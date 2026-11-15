from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL


class CodeEmbedding:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )


    def embed_documents(self, chunks):

        texts = []

        metadatas = []

        for chunk in chunks:

            texts.append(
                chunk["content"]
            )

            metadatas.append(
                {
                    "path": chunk["path"],
                    "language": chunk["language"],
                    "chunk_id": chunk["chunk_id"]
                }
            )


        embeddings = self.embedding_model.embed_documents(
            texts
        )


        return embeddings, texts, metadatas



    def embed_query(self, query):

        embedding = self.embedding_model.embed_query(
            query
        )

        return embedding