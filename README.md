# StrokeGene

## Research Background

With the in-depth research on stroke, a vast amount of academic literature has emerged, posing significant challenges for researchers in literature retrieval, information filtering, and academic organization. To help researchers more efficiently access and understand the latest research findings related to stroke, we developed this intelligent assistant for stroke research. Based on large language models (LLMs) and natural language processing (NLP) technologies, this assistant helps users quickly query and analyze relevant literature, providing intelligent support for stroke academic research.

![image](https://github.com/user-attachments/assets/85ce26d7-85dc-4d7d-b307-6920be3cf361)


## Environment Setup

**Create Environment**

```
conda create --name StrokeGene python=3.9
```

**Activate Environment**

```
conda activate StrokeGene
```

**Install Required Libraries**

```
pip install requirements.txt
```

**Download the Necessary Embeddings Locally**

m3e

[moka-ai/m3e-base · Hugging Face](https://huggingface.co/moka-ai/m3e-base)

SapBERT-from-PubMedBERT-fulltext

[cambridgeltl/SapBERT-from-PubMedBERT-fulltext · Hugging Face](https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext)

Download Word Vectors (Chroma)

https://drive.google.com/drive/folders/1S7CF4y1KeT50c4VkWkR7ETWtnzgpkrM3?usp=sharing

Save the files into the vector_db folder (if vector_db does not exist, create it in the project root directory).

**Modify with Your Own API Keys**

The project uses Baidu's Wenxin Yiyan API.

```
修改地址为 util中的key.py
class KEY:
     wenxin_api_key="xxx" # Enter your own Wenxin Yiyan API key here
     wenxin_secret_key="xxx"# Enter your own Wenxin Yiyan secret key here
```

**Start the Application**

```
cd serve
python run_gradio.py
```

## Demo Interface

![image](https://github.com/user-attachments/assets/cacb4ce4-49ef-4d59-a372-c22a44cc9cbd)


#### 致谢

感谢[动手学大模型应用开发](https://datawhalechina.github.io/llm-universe/#/)所提供的教学方法。

