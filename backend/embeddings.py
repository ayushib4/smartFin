import openai
from backend.constants import EMBEDDING_MODEL


def get_embedding(input, model=EMBEDDING_MODEL):
    # text = text.replace("\n", " ")
    return openai.Embedding.create(input=[input], model=model)["data"][0]["embedding"]
