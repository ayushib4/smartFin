from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    def __init__(self, model_id="multi-qa-MiniLM-L6-cos-v1"):
        self.model = SentenceTransformer(model_id, cache_folder="embedder")

    def embed(self, input: str, debug=False) -> list[float]:
        embeddings = self.model.encode(input, show_progress_bar=debug)
        return embeddings.tolist()

    def get_dimensions(self) -> int:
        return self.model.get_sentence_embedding_dimension() or -1
