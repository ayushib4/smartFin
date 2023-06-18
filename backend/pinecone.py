from os import getenv
import pinecone
from backend.constants import DIMENSIONS
from backend.embeddings import get_embedding

PINECONE_API_KEY = getenv("PINECONE_API_KEY")
PINECONE_ENV = getenv("PINECONE_ENVIRONMENT")
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)


def create_pinecone_index(user_id):
    metadata_config = {}
    # with the metadata config, pinecone will only filter with the provided metadata field(s)
    pinecone.create_index(
        f"{user_id}-transactions", dimension=DIMENSIONS, metadata_config=metadata_config
    )
    return


def store_embeddings(user_id, data):
    assert (
        f"{user_id}-transactions" in pinecone.list_indexes()
    ), f"Could not find an index in Pinecone for {user_id}"
    index = pinecone.Index(f"{user_id}-transactions")
    batch_size = 100  # how many embeddings we create and insert at once
    upsert_response = [] * len(data)

    for i in range(0, len(data), batch_size):
        upsert_response[i] = (
            data[i]["transaction_id"],
            get_embedding(data[i]),
            {data[i]},
        )

    index.upsert(vectors=upsert_response)


def construct_prompt(user_id, query):
    query_embedding = get_embedding(query)
    index = pinecone.Index(f"{user_id}-transactions")
    response = index.query(query_embedding, top_k=5, include_metadata=True)
    return response 
    contexts = [x["metadata"]["inference"] for x in response["matches"]] # replace inference with fields relevant for contexts 
