from sentence_transformers import CrossEncoder

from config import RERANKER_MODEL


class ReRanker:

    def __init__(self):

        self.model = CrossEncoder(
            RERANKER_MODEL
        )

    def rerank(self, query, documents, top_k=5):

        if not documents:
            return []

        sentence_pairs = []

        for document in documents:

            sentence_pairs.append(
                (
                    query,
                    document["content"]
                )
            )

        scores = self.model.predict(
            sentence_pairs
        )

        ranked_documents = []

        for score, document in zip(scores, documents):

            ranked_documents.append(
                {
                    "score": float(score),
                    "content": document["content"],
                    "metadata": document["metadata"]
                }
            )

        ranked_documents.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked_documents[:top_k]