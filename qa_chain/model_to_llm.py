import sys 
sys.path.append("../llm")
from llm.wenxin_llm import Wenxin_LLM
from util import KEY

def model_to_llm(model:str=None, temperature:float=0.0):
        # 加载文心一言语言模型
        llm = Wenxin_LLM(model=model, temperature = temperature, api_key=KEY.wenxin_api_key, secret_key=KEY.wenxin_secret_key)
        return llm