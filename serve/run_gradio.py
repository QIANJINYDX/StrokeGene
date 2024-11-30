# 导入必要的库

import sys
import os                # 用于操作系统相关的操作，例如读取环境变量

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import IPython.display   # 用于在 IPython 环境中显示数据，例如图片
import io                # 用于处理流式数据（例如文件流）
import gradio as gr
from dotenv import load_dotenv, find_dotenv
from llm.call_llm import get_completion
from database.create_db import create_db_info
from qa_chain.Chat_QA_chain_self import Chat_QA_chain_self
from qa_chain.QA_chain_self import QA_chain_self
import re
# 导入 dotenv 库的函数
# dotenv 允许您从 .env 文件中读取环境变量
# 这在开发时特别有用，可以避免将敏感信息（如API密钥）硬编码到代码中

# 寻找 .env 文件并加载它的内容
# 这允许您使用 os.environ 来读取在 .env 文件中设置的环境变量
_ = load_dotenv(find_dotenv())
LLM_MODEL_DICT = {
    "wenxin": ["ERNIE-Speed-128K", "ERNIE-Speed-8K"],
}


LLM_MODEL_LIST = sum(list(LLM_MODEL_DICT.values()),[])
INIT_LLM = "ERNIE-Speed-128K"
EMBEDDING_MODEL_LIST = ['pubmed','m3e']
INIT_EMBEDDING_MODEL = "m3e"
DEFAULT_DB_PATH = "knowledge_db"
DEFAULT_PERSIST_PATH = "vector_db/chroma"

def get_model_by_platform(platform):
    return LLM_MODEL_DICT.get(platform, "")
class Model_center():
    """
    存储问答 Chain 的对象 

    - chat_qa_chain_self: 以 (model, embedding) 为键存储的带历史记录的问答链。
    - qa_chain_self: 以 (model, embedding) 为键存储的不带历史记录的问答链。
    """
    def __init__(self):
        self.chat_qa_chain_self = {}
        self.qa_chain_self = {}

    def chat_qa_chain_self_answer(self, question: str, chat_history: list = [], model: str = "openai", embedding: str = "openai", temperature: float = 0.0, top_k: int = 4, history_len: int = 3, file_path: str = DEFAULT_DB_PATH, persist_path: str = DEFAULT_PERSIST_PATH):
        """
        调用带历史记录的问答链进行回答
        """
        if question == None or len(question) < 1:
            return "", chat_history
        try:
            if (model, embedding) not in self.chat_qa_chain_self:
                self.chat_qa_chain_self[(model, embedding)] = Chat_QA_chain_self(model=model, temperature=temperature,
                                                                                    top_k=top_k, chat_history=chat_history, file_path=file_path, persist_path=persist_path, embedding=embedding)
            chain = self.chat_qa_chain_self[(model, embedding)]
            return "", chain.answer(question=question, temperature=temperature, top_k=top_k)
        except Exception as e:
            return e, chat_history

    def qa_chain_self_answer(self, question: str, chat_history: list = [], model: str = "openai", embedding="openai", temperature: float = 0.0, top_k: int = 4, file_path: str = DEFAULT_DB_PATH, persist_path: str = DEFAULT_PERSIST_PATH):
        """
        调用不带历史记录的问答链进行回答
        """
        if question == None or len(question) < 1:
            return "", chat_history, ""  # 返回空字符串作为占位符
        try:
            if (model, embedding) not in self.qa_chain_self:
                self.qa_chain_self[(model, embedding)] = QA_chain_self(model=model, temperature=temperature,
                                                                    top_k=top_k, file_path=file_path, persist_path=persist_path, embedding=embedding)
            chain = self.qa_chain_self[(model, embedding)]
            answer, source_documents = chain.answer(question, temperature, top_k)
            chat_history.append((question, answer))

            # 从 source_documents 提取出相关的元数据
            source_documents = [str(doc.metadata['source']) for doc in source_documents]
            return answer, chat_history, source_documents  # 返回 answer, chat_history 和 source_documents_display
        except Exception as e:
            return str(e), chat_history, ""  # 错误时返回空字符串作为占位符

    def clear_history(self):
        if len(self.chat_qa_chain_self) > 0:
            for chain in self.chat_qa_chain_self.values():
                chain.clear_history()


def format_chat_prompt(message, chat_history):
    """
    该函数用于格式化聊天 prompt。

    参数:
    message: 当前的用户消息。
    chat_history: 聊天历史记录。

    返回:
    prompt: 格式化后的 prompt。
    """
    # 初始化一个空字符串，用于存放格式化后的聊天 prompt。
    prompt = ""
    # 遍历聊天历史记录。
    for turn in chat_history:
        # 从聊天记录中提取用户和机器人的消息。
        user_message, bot_message = turn
        # 更新 prompt，加入用户和机器人的消息。
        prompt = f"{prompt}\nUser: {user_message}\nAssistant: {bot_message}"
    # 将当前的用户消息也加入到 prompt中，并预留一个位置给机器人的回复。
    prompt = f"{prompt}\nUser: {message}\nAssistant:"
    # 返回格式化后的 prompt。
    return prompt



def respond(message, chat_history, llm, history_len=3, temperature=0.1, max_tokens=2048):
    """
    该函数用于生成机器人的回复。

    参数:
    message: 当前的用户消息。
    chat_history: 聊天历史记录。

    返回:
    "": 空字符串表示没有内容需要显示在界面上，可以替换为真正的机器人回复。
    chat_history: 更新后的聊天历史记录
    """
    if message == None or len(message) < 1:
            return "", chat_history
    try:
        # 限制 history 的记忆长度
        chat_history = chat_history[-history_len:] if history_len > 0 else []
        # 调用上面的函数，将用户的消息和聊天历史记录格式化为一个 prompt。
        formatted_prompt = format_chat_prompt(message, chat_history)
        # 使用llm对象的predict方法生成机器人的回复（注意：llm对象在此代码中并未定义）。
        bot_message = get_completion(
            formatted_prompt, llm, temperature=temperature, max_tokens=max_tokens)
        # 将bot_message中\n换为<br/>
        bot_message = re.sub(r"\\n", '<br/>', bot_message)
        # 将用户的消息和机器人的回复加入到聊天历史记录中。
        chat_history.append((message, bot_message))
        # 返回一个空字符串和更新后的聊天历史记录（这里的空字符串可以替换为真正的机器人回复，如果需要显示在界面上）。
        return "", chat_history
    except Exception as e:
        return e, chat_history


model_center = Model_center()

block = gr.Blocks()
with block as demo:
    with gr.Row(equal_height=True):
        with gr.Column(scale=2):
            gr.Markdown("""<h1><center>Stroke Gene</center></h1>""")
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(height=400, show_copy_button=True, show_share_button=True)
            msg = gr.Textbox(label="Prompt/问题")

            with gr.Row():
                # db_with_his_btn = gr.Button("Chat db with history")
                db_wo_his_btn = gr.Button("Chat db without history")
                # llm_btn = gr.Button("Chat with llm")
            with gr.Row():
                clear = gr.ClearButton(components=[chatbot], value="Clear console")

        with gr.Column(scale=1):
            file = gr.File(label='请选择知识库目录', file_count='directory', file_types=['.txt', '.md', '.docx', '.pdf'])
            with gr.Row():
                init_db = gr.Button("知识库文件向量化")
            model_argument = gr.Accordion("参数配置", open=False)
            with model_argument:
                temperature = gr.Slider(0, 1, value=0.01, step=0.01, label="llm temperature", interactive=True)
                top_k = gr.Slider(1, 10, value=3, step=1, label="vector db search top k", interactive=True)
                history_len = gr.Slider(0, 5, value=3, step=1, label="history length", interactive=True)

            model_select = gr.Accordion("模型选择")
            with model_select:
                llm = gr.Dropdown(LLM_MODEL_LIST, label="large language model", value=INIT_LLM, interactive=True)
                embeddings = gr.Dropdown(EMBEDDING_MODEL_LIST, label="Embedding model", value=INIT_EMBEDDING_MODEL)

        # 新增一个组件，用于显示 source_documents
        source_docs_display = gr.File(label="参考文献")  # 显示 source_documents
        
        
        # 设置初始化向量数据库按钮的点击事件
        init_db.click(create_db_info, inputs=[file, embeddings], outputs=[msg])

        # 设置按钮的点击事件
        # db_with_his_btn.click(model_center.chat_qa_chain_self_answer, inputs=[msg, chatbot, llm, embeddings, temperature, top_k, history_len], outputs=[msg, chatbot])
        db_wo_his_btn.click(model_center.qa_chain_self_answer, inputs=[msg, chatbot, llm, embeddings, temperature, top_k], outputs=[msg, chatbot, source_docs_display])
        # llm_btn.click(respond, inputs=[msg, chatbot, llm, history_len, temperature], outputs=[msg, chatbot], show_progress="minimal")
        msg.submit(respond, inputs=[msg, chatbot, llm, history_len, temperature], outputs=[msg, chatbot], show_progress="hidden")
        clear.click(model_center.clear_history)

    gr.Markdown("""提醒：<br>
    1. 项目会解析自带的知识库，如何你想使用自己的知识文件请重新上传。
    2. 初始化数据库时间可能较长，请耐心等待。
    3. 使用中如果出现异常，将会在文本输入框进行展示，请不要惊慌。 
    4. 请使用英文进行提问，方便检索到相应知识           
    <br>
    """)
# threads to consume the request
gr.close_all()
demo.launch()