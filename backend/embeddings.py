# import openai
# from constants import EMBEDDING_MODEL


# def get_embedding(input, model=EMBEDDING_MODEL):
#     # text = text.replace("\n", " ")
#     return openai.Embedding.create(input=[input], model=model)["data"][0]["embedding"]
from os import getenv
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import numpy as np

load_dotenv()

model_id = "multi-qa-MiniLM-L6-cos-v1"

hf_token = getenv("HF_TOKEN")

def get_embedding(input, model_id=model_id):
    embedder = SentenceTransformer(model_id, cache_folder='embedder')
    embeddings = embedder.encode(input)
    return embeddings.tolist()