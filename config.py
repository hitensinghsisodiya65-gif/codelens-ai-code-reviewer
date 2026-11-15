import os
from dotenv import load_dotenv

load_dotenv()
# =============================
# API Configuration
# =============================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# =============================
# Model Configuration
# =============================

MODEL_NAME = "openai/gpt-oss-120b"

# =============================
# Embedding Configuration
# =============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# =============================
# Vector Database
# =============================

FAISS_INDEX_PATH = "faiss_index"

# =============================
# Chunking
# =============================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"