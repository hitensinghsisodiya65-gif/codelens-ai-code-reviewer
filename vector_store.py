import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None

        self.documents = []

        self.metadatas = []


    def add_documents(self, embeddings, texts, metadatas):

        vectors = np.array(
            embeddings
        ).astype("float32")


        dimension = vectors.shape[1]


        if self.index is None:

            self.index = faiss.IndexFlatIP(
                dimension
            )


        self.index.add(
            vectors
        )


        self.documents.extend(
            texts
        )


        self.metadatas.extend(
            metadatas
        )


    def search(self, query_embedding, k=5):

        if self.index is None:

            return []


        query_vector = np.array(
            [query_embedding]
        ).astype("float32")


        scores, indices = self.index.search(
            query_vector,
            k
        )


        results = []


        for score, index in zip(
            scores[0],
            indices[0]
        ):

            if index == -1:
                continue


            results.append(
                {
                    "content": self.documents[index],
                    "metadata": self.metadatas[index],
                    "score": float(score)
                }
            )


        return results