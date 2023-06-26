from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    A SentenceTransformer wrapper for encoding strings into vectors
    """

    def __init__(self, model_id="multi-qa-MiniLM-L6-cos-v1"):
        self.model = SentenceTransformer(model_id, cache_folder="embedder")

    def embed(self, input: str, debug=False) -> list[float]:
        embeddings = self.model.encode(input, show_progress_bar=debug)
        return embeddings.tolist()  # type: ignore

    def get_dimensions(self) -> int:
        if not (dim := self.model.get_sentence_embedding_dimension()):
            raise ValueError(
                f"Sentence embedding model returned invalid/no dimension: {dim}"
            )

        return dim
