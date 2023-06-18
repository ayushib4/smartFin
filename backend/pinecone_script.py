import time
import pinecone
from os import getenv
from constants import PROMPT_EXAMPLES, EXAMPLE_USER_ID, EXAMPLE_TRANSACTIONS
from inference import InferenceModel
from constants import DIMENSIONS
from embeddings import get_embedding
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = getenv("PINECONE_API_KEY")
PINECONE_ENV = getenv("PINECONE_ENV")
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)


def create_pinecone_index():
    if "transaction" in pinecone.list_indexes():
        return

    metadata_config = {"indexed": ["user_id"]}
    # with the metadata config, pinecone will only filter with the provided metadata field(s)
    pinecone.create_index(
        "transaction", dimension=DIMENSIONS, metadata_config=metadata_config
    )
    print(f"Created pinecone index called 'transaction'")
    return


def prepare_data_for_embedding(json_data):
    strs: list[str] = []
    categories = [
        "amount",
        "authorized_date",
        "authorized_datetime",
        "category",
        "date",
        "datetime",
        "location",
        "merchant_name",
        "name",
        "payment_channel",
        "personal_finance_category",
    ]

    for category in categories:
        if category not in json_data:
            print(f"WARNING: {category} not found in transaction JSON")
            continue

        category_data = json_data[category]

        if category == "location":
            strs.append(
                f"{category}: {category_data['address']}, {category_data['city']}, {category_data['country']}, {category_data['postal_code']}."
            )
        elif category == "personal_finance_category":
            strs.append(f"{category}: {category_data['detailed']}.")
        else:
            strs.append(f"{category}: {category_data}.")

    return " ".join(strs)


def store_embeddings(user_id, data):
    assert (
        "transaction" in pinecone.list_indexes()
    ), f"Could not find the transaction indexs"

    model = InferenceModel(prompt_examples=PROMPT_EXAMPLES)
    index = pinecone.Index(f"transaction")
    batch_size = 128  # how many embeddings we create and insert at once

    for i in range(0, len(data), batch_size):
        vectors = [""] * min(len(data) - i, batch_size)
        for j in range(i, min(len(data), i + batch_size)):
            string_data = prepare_data_for_embedding(data[j])

            print("Inference start " + str(time.time()))

            inferred_data = model.infer_from_transaction(string_data)

            print("Inference end " + str(time.time()))

            vectors[j] = (
                data[j]["transaction_id"],
                get_embedding(string_data + inferred_data),
                {"user_id": user_id, "inference": inferred_data},
            )

            print("Emedding start " + str(time.time()))
        index.upsert(vectors=vectors)

    print(f"Stored openai embeddings in pinecone")


def construct_prompt(user_id, query):
    query_embedding = get_embedding(query)

    index = pinecone.Index(f"transaction")
    response = index.query(
        query_embedding,
        top_k=1,
        filter={"user_id": {"$eq": user_id}},
        include_metadata=True,
    )
    result = [x["metadata"]["inference"] for x in response["matches"]]
    print(result)
    return result

    print(response)
    return response
    contexts = [
        x["metadata"]["inference"] for x in response["matches"]
    ]  # replace inference with fields relevant for contexts


def init_pinecone(user_id: str, transaction_infs: list[dict]) -> None:
    create_pinecone_index()
    print("Done indexing " + str(time.time()))
    store_embeddings(user_id, transaction_infs)


def update_pinecone(user_id: str, transaction_infs: list[dict]) -> None:
    store_embeddings(user_id, transaction_infs)


def query_pinecone(user_id: str, query: str) -> None:
    construct_prompt(user_id, query)


if __name__ == "__main__":
    print("Start " + str(time.time()))
    init_pinecone(EXAMPLE_USER_ID, EXAMPLE_TRANSACTIONS)
    print("Done storing " + str(time.time()))
    query_pinecone(EXAMPLE_USER_ID, "What is my most stupid purchase?")
    print("Done querying " + str(time.time()))
