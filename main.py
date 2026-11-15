from parser import ProjectParser
from chunker import CodeChunker
from embedding import CodeEmbedding
from vector_store import VectorStore
from semantic_search import SemanticSearch

from agent import Agent


class CodeReviewer:

    def __init__(self):

        self.parser = ProjectParser()

        self.chunker = CodeChunker()

        self.embedding = CodeEmbedding()

        self.vector_store = VectorStore()

        self.agent = Agent()

    def load_project(self, project_path):

        # Parse project files
        documents = self.parser.parse_project(
            project_path
        )

        # Split into chunks
        chunks = self.chunker.chunk_documents(
            documents
        )

        # Convert chunks into embeddings
        texts, metadatas, embedding_model = self.embedding.embed_documents(
            chunks
        )

        # Store in FAISS
        self.vector_store.add_documents(
            texts,
            metadatas,
            embedding_model
        )

        # Create Semantic Search
        semantic_search = SemanticSearch(
            self.embedding,
            self.vector_store
        )

        # Save into memory
        self.agent.memory.set_project(
            project_path
        )

        self.agent.memory.set_semantic_search(
            semantic_search
        )

    def chat(self, query):

        return self.agent.chat(query)