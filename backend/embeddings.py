from os import getenv
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from constants import EMBEDDING_MODEL

load_dotenv()

hf_token = getenv("HF_TOKEN")


def get_embedding(input, model_id=EMBEDDING_MODEL):
    embedder = SentenceTransformer(model_id, cache_folder="embedder")
    embeddings = embedder.encode(input)
    return embeddings.tolist()
