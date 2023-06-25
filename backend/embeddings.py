from sentence_transformers import SentenceTransformer
from torch import Tensor

from constants import EMBEDDING_MODEL


class EmbeddingModel:
    def __init__(self, model_id=EMBEDDING_MODEL):
        self.model = SentenceTransformer(model_id, cache_folder="embedder")

    def embed(self, input: str, debug=False) -> list[float]:
        embeddings = self.model.encode(input, show_progress_bar=debug)
        return embeddings.tolist()

    def get_dimensions(self) -> int:
        return self.model.get_sentence_embedding_dimension() or -1
