import time
import pinecone
from os import getenv
from constants import (
    PROMPT_EXAMPLES,
    EXAMPLE_LESS_USER_ID,
    EXAMPLE_LESS_TRANSACTIONS,
)
from inference import InferenceModel
from embeddings import EmbeddingModel
from dotenv import load_dotenv

load_dotenv()

PINECONE_INDEX = "transactions"
BATCH_SIZE = 128
EMBEDDABLE_FIELDS = [
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


class UserTransactionsInterface:
    """
    A database interface for semantic search on user transactions
    """

    def __init__(
        self,
        user_id: str,
        inference_model: InferenceModel,
        embedding_model: EmbeddingModel,
    ) -> None:
        pinecone.init(
            api_key=getenv("PINECONE_API_KEY") or "",
            environment=getenv("PINECONE_ENV") or "",
        )

        self.user_id = user_id
        self._inference_model = inference_model
        self._embedding_model = embedding_model

        if not self.is_indexed():
            self._create_index()

        self.index = pinecone.Index(PINECONE_INDEX)

    def _create_index(self) -> None:
        pinecone.create_index(
            PINECONE_INDEX,
            dimension=self._embedding_model.get_dimensions(),
            metadata_config={"indexed": ["user_id"]},
        )

        print(f"Created Pinecone index.")

        return

    def add_transactions(self, transactions: list[dict]) -> None:
        assert self.is_indexed()

        num_transactions = len(transactions)

        for i in range(0, num_transactions, BATCH_SIZE):
            vectors: list[tuple[str, str, dict]] = []

            for j in range(i, min(num_transactions, i + BATCH_SIZE)):
                data = self._stringify_transaction(transactions[j])

                # print("Inference start " + str(time.time()))

                # inference = self._inference_model.infer(transaction)

                # print("Inference end " + str(time.time()))

                vectors.append(
                    (
                        transactions[j]["transaction_id"],
                        self._embedding_model.embed(data),
                        {"user_id": self.user_id, "data": data},
                    )
                )

            self.index.upsert(vectors)

        print(f"Finished adding {num_transactions} transactions.")

    def _stringify_transaction(self, transaction: dict) -> str:
        assert self.is_indexed()

        strs: list[str] = []

        for field in EMBEDDABLE_FIELDS:
            if field not in transaction:
                print(f"WARNING: {field} does not exist in {transaction}")
                continue

            data = transaction[field]

            if field == "location":
                strs.append(
                    f"{field}: {data['address']}, {data['city']}, {data['country']}, {data['postal_code']}."
                )
            elif field == "personal_finance_category":
                strs.append(f"{field.capitalize()}: {data['detailed']}.")
            else:
                strs.append(f"{field.capitalize()}: {data}.")

        return " ".join(strs)

    def query(self, query: str, num_results=1) -> list[dict[float, str]]:
        assert self.is_indexed()

        query_embedding = self._embedding_model.embed(query)

        responses = self.index.query(
            query_embedding,
            top_k=num_results,
            filter={"user_id": {"$eq": self.user_id}},
            include_metadata=True,
        )["matches"]

        return [{r["score"]: f"{r['metadata']['data']}"} for r in responses]  # type: ignore

    def is_indexed(self) -> bool:
        return PINECONE_INDEX in pinecone.list_indexes()


if __name__ == "__main__":
    print("Start " + str(time.time()))

    transactions_interface = UserTransactionsInterface(
        EXAMPLE_LESS_USER_ID,
        InferenceModel(prompt_examples=PROMPT_EXAMPLES),
        EmbeddingModel(),
    )

    transactions_interface.add_transactions(EXAMPLE_LESS_TRANSACTIONS)
    print("Done storing " + str(time.time()))
    response = transactions_interface.query("What is my most stupid purchase?")
    print(response)
    print("Done querying " + str(time.time()))
