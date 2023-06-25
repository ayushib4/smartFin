import time
from typing import Iterable
import pinecone
from os import getenv
from data_constants import (
    PROMPT_EXAMPLES,
    EXAMPLE_USER_ID,
    EXAMPLE_TRANSACTIONS,
)
from inference import InferenceModel
from embedding import EmbeddingModel
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


class TransactionsInterface:
    """
    A database interface for semantic search on user transactions
    """

    def __init__(
        self,
        inference_model: InferenceModel,
        embedding_model: EmbeddingModel,
    ) -> None:
        pinecone.init(
            api_key=getenv("PINECONE_API_KEY") or "",
            environment=getenv("PINECONE_ENV") or "",
        )

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

    def add_transactions(self, user_id: str, transactions: Iterable[dict]) -> None:
        assert self.is_indexed()

        vectors: list[tuple[str, str, dict]] = []
        count = 0

        for transaction in transactions:
            if count > 0 and count % BATCH_SIZE == 0:
                self.index.upsert(vectors)
                vectors.clear()
                continue

            transaction_str = self._stringify_transaction(transaction)

            vectors.append(
                (
                    transaction["transaction_id"],
                    self._embedding_model.embed(transaction_str),
                    {"user_id": user_id, "transaction": transaction_str},
                )
            )

            count += 1

        print(f"Added {count} transactions.")

    def _stringify_transaction(self, transaction: dict) -> str:
        assert self.is_indexed()

        strs: list[str] = []

        for field in EMBEDDABLE_FIELDS:
            if field not in transaction:
                print(f"WARNING: {field} does not exist in {transaction}")
                continue

            data = transaction[field]

            formatted_field = field.replace("_", " ").title()

            if field == "location":
                strs.append(
                    f"{field}: {data['address']}, {data['city']}, {data['country']}, {data['postal_code']}."
                )
            elif field == "personal_finance_category":
                strs.append(f"{formatted_field}: {data['detailed']}.")
            else:
                strs.append(f"{formatted_field}: {data}.")

        return " ".join(strs)

    def query(self, user_id: str, query: str, num_results=5) -> list[dict[float, str]]:
        assert self.is_indexed()

        query_embedding = self._embedding_model.embed(query)

        responses = self.index.query(
            query_embedding,
            top_k=num_results,
            filter={"user_id": {"$eq": user_id}},
            include_metadata=True,
        )["matches"]

        return [{r["score"]: f"{r['metadata']['transaction']}"} for r in responses]  # type: ignore

    def is_indexed(self) -> bool:
        return PINECONE_INDEX in pinecone.list_indexes()


if __name__ == "__main__":
    print("Start " + str(time.time()))

    transactions_interface = TransactionsInterface(
        InferenceModel(prompt_examples=PROMPT_EXAMPLES),
        EmbeddingModel(),
    )

    transactions_interface.add_transactions(EXAMPLE_USER_ID, EXAMPLE_TRANSACTIONS)
    print("Done storing " + str(time.time()))
    response = transactions_interface.query(
        EXAMPLE_USER_ID, "What is my most stupid purchase?"
    )
    print(response)
    print("Done querying " + str(time.time()))
