from time import time
from typing import Iterable
from os import getenv
from data_constants import (
    EXAMPLE_USER_ID,
    EXAMPLE_TRANSACTIONS,
)
from inference import InferenceModel
from embedding import EmbeddingModel
from dotenv import load_dotenv

import pinecone
from concurrent.futures import ProcessPoolExecutor, wait

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

        if PINECONE_INDEX not in pinecone.list_indexes():
            pinecone.create_index(
                PINECONE_INDEX,
                dimension=self._embedding_model.get_dimensions(),
                metadata_config={"indexed": ["user_id"]},
            )

            print(f"Created Pinecone index {PINECONE_INDEX}.")

        self.index = pinecone.Index(PINECONE_INDEX)

    def _add_transaction(self, user_id: str, transaction: dict):
        transaction_str = self._stringify_transaction(transaction)
        inference_str = self._inference_model.infer(transaction_str)

        self.index.upsert(
            [
                transaction["transaction_id"],
                self._embedding_model.embed(transaction_str + inference_str),
                {
                    "user_id": user_id,
                    "transaction": transaction_str,
                    "inference": inference_str,
                },
            ]
        )

    def add_transactions(self, user_id: str, transactions: Iterable[dict]) -> None:
        executor = ProcessPoolExecutor(10)
        wait(
            [
                executor.submit(self._add_transaction, user_id, transaction)
                for transaction in transactions
            ]
        )

    def _stringify_transaction(self, transaction: dict) -> str:
        field_strs: list[str] = []

        for field in EMBEDDABLE_FIELDS:
            if field not in transaction:
                print(f"WARNING: {field} does not exist in {transaction}")
                continue

            data = transaction[field]

            formatted_field = field.replace("_", " ").title()

            if field == "location":
                field_strs.append(
                    f"{field}: {data['address']}, {data['city']}, {data['country']}, {data['postal_code']}."
                )
            elif field == "personal_finance_category":
                field_strs.append(f"{formatted_field}: {data['detailed']}.")
            else:
                field_strs.append(f"{formatted_field}: {data}.")

        return " ".join(field_strs)

    def query(self, user_id: str, query: str, num_results=5) -> list[dict[float, str]]:
        query_embedding = self._embedding_model.embed(query)

        responses = self.index.query(
            query_embedding,
            top_k=num_results,
            filter={"user_id": {"$eq": user_id}},
            include_metadata=True,
        )["matches"]

        return [{r["score"]: f"{r['metadata']['transaction']}"} for r in responses]  # type: ignore


if __name__ == "__main__":
    start_time = time()

    transactions_interface = TransactionsInterface(
        InferenceModel(),
        EmbeddingModel(),
    )

    print(f"Initialized TransactionsInterface in {time() - start_time}s.")

    transactions_interface.add_transactions(EXAMPLE_USER_ID, EXAMPLE_TRANSACTIONS)

    response = transactions_interface.query(
        EXAMPLE_USER_ID, "What is my most stupid purchase?"
    )

    print(response)

    print(f"Completed test in {time() - start_time}s.")
