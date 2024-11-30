import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from langchain.embeddings.huggingface import HuggingFaceEmbeddings

def get_embedding(embedding: str):
    if embedding == 'm3e':
        return HuggingFaceEmbeddings(model_name="m3e-base")
    elif embedding == "pubmed":
        return HuggingFaceEmbeddings(model_name="SapBERT-from-PubMedBERT-fulltext")
