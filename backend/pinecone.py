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
            {data[i]["inference"]},
        )

    index.upsert(vectors=upsert_response)


def construct_prompt(user_id, query):
    query_embedding = get_embedding(query)
    index = pinecone.Index(f"{user_id}-transactions")
    response = index.query(query_embedding, top_k=3, include_metadata=True)
    contexts = [x["metadata"]["inference"] for x in response["matches"]]

def semantic_search(user_id):
    # now connect to the index
    index = pinecone.GRPCIndex(f"{user_id}")

    batch_size = 128
    questions = []  # list of questions

    for i in tqdm(range(0, len(questions), batch_size)):
        # find end of batch
        i_end = min(i + batch_size, len(questions))
        # create IDs batch
        ids = [str(x) for x in range(i, i_end)]
        # create metadata batch
        metadatas = [{"text": text} for text in questions[i:i_end]]
        # create embeddings
        xc = get_embedding(questions[i:i_end])
        # create records list for upsert
        records = zip(ids, xc, metadatas)
        # upsert to Pinecone
        index.upsert(vectors=records)

    # check number of records in the index
    index.describe_index_stats()

    query = "which city has the highest population in the world?"

    # create the query vector
    xq = get_embedding(query).tolist()

    # now query
    xc = index.query(xq, top_k=5, include_metadata=True)
    return xc
