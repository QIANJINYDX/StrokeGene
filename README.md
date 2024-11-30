# StrokeGene

## 研究背景

随着脑卒中研究的深入，海量的学术文献涌现出来，科研工作者面临着文献检索、信息筛选和学术整理的巨大挑战。为了帮助科研人员更高效地获取和理解与脑卒中相关的最新研究成果，我们开发了这款脑卒中智能助手。该助手基于大语言模型（LLM）和自然语言处理（NLP）技术，能够帮助用户快速查询和分析相关文献，为脑卒中的学术研究提供智能支持。

![LLM](F:\Program\Python\IS\文档\LLM.png)

## 环境搭建

**创建环境**

```
conda create --name StrokeGene python=3.9
```

**激活环境**

```
conda activate StrokeGene
```

**安装需求库**

```
pip install requirements.txt
```

**将所需要的Embedding下载到本地**

m3e

[moka-ai/m3e-base · Hugging Face](https://huggingface.co/moka-ai/m3e-base)

SapBERT-from-PubMedBERT-fulltext

[cambridgeltl/SapBERT-from-PubMedBERT-fulltext · Hugging Face](https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext)

下载词向量chroma

https://drive.google.com/drive/folders/1S7CF4y1KeT50c4VkWkR7ETWtnzgpkrM3?usp=sharing

并将文件保存到vector_db内

**修改为自己key**

项目使用的是百度的文心一言

```
修改地址为 util中的key.py
class KEY:
     wenxin_api_key="xxx" # 此处填写你申请的文心一言的api_key
     wenxin_secret_key="xxx"# 此处填写你申请的文心一言的secret_key
```

**启动运行**

```
cd serve
python run_gradio.py
```

## 演示界面

![image-20241130194514072](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20241130194514072.png)

#### 致谢

感谢[动手学大模型应用开发](https://datawhalechina.github.io/llm-universe/#/)所提供的教学方法。

