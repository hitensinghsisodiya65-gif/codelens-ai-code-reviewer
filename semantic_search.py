class SemanticSearch:

    def __init__(self, embedding, vector_store):

        self.embedding = embedding

        self.vector_store = vector_store

    def search(self, query, k=5):

        query_embedding = self.embedding.embed_query(
            query
        )

        results = self.vector_store.search(
            query_embedding,
            k
        )

        return results