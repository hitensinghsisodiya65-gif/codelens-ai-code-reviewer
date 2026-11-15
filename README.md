# CodeLens – AI Code Review Agent

An AI-powered code review assistant designed to analyze software projects, understand codebases, investigate bugs, and provide contextual code insights using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and specialized AI agents.

## Overview

CodeLens allows developers to load a software project and interact with an AI assistant to explore and analyze its code.

It uses code parsing, chunking, embeddings, semantic retrieval, reranking, and AI-powered analysis to generate responses based on relevant project context.

The system is organized into specialized modules for different code analysis tasks, including debugging, optimization, and security analysis.

## Features

- **Project Analysis:** Load and explore software projects.
- **AI Code Review:** Analyze code and identify potential improvements.
- **Debugging Assistant:** Investigate errors and understand possible causes.
- **Code Optimization:** Explore code quality and optimization opportunities.
- **Security Analysis:** Examine potential security concerns.
- **RAG Pipeline:** Retrieve relevant code context before generating responses.
- **Semantic Search:** Find relevant code using embeddings.
- **Reranking:** Improve the relevance of retrieved code context.
- **Conversational Memory:** Maintain conversation context.
- **Web Interface:** Interact with the AI assistant through a browser.
- **ZIP Upload:** Load projects through ZIP archives.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application and AI logic |
| FastAPI | Backend API |
| HTML | Frontend |
| CSS | Interface styling |
| JavaScript | Frontend interactions |
| Groq API | LLM inference |
| LangChain | LLM integration |
| Embeddings | Code representation |
| Vector Store | Semantic retrieval |
| RAG | Context-aware responses |

## Architecture

```text
                  USER
                    |
                    v
               CodeLens UI
                    |
                    v
               FastAPI
                    |
                    v
              Code Reviewer
                    |
          +---------+---------+
          |                   |
          v                   v
      Code Parser          AI Router
          |                   |
          v                   v
       Chunker          Specialized Agents
          |             /      |       \
          v          Debug   Optimize  Security
      Embedding
          |
          v
      Vector Store
          |
          v
      Semantic Search
          |
          v
       Reranker
          |
          v
     Context Builder
          |
          v
         LLM
          |
          v
      AI Response
```

## Project Structure

```text
AI Code Review Agent/
│
├── static/
│   └── index.html
│
├── agent.py
├── app.py
├── assistant.py
├── chunker.py
├── config.py
├── context_builder.py
├── debugger.py
├── embedding.py
├── llm.py
├── main.py
├── memory.py
├── optimizer.py
├── parser.py
├── prompt.py
├── reranker.py
├── reviewer.py
├── router.py
├── security.py
├── semantic_search.py
├── server.py
├── vector_store.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/codelens-ai-code-reviewer.git
cd codelens-ai-code-reviewer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never upload your actual API key or `.env` file to GitHub.

### 5. Run the Application

```bash
uvicorn server:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## How It Works

1. A user loads a software project.
2. The parser processes supported source files.
3. The chunker divides code into smaller sections.
4. The embedding module converts code chunks into vector representations.
5. The vector store stores information for retrieval.
6. Semantic search retrieves relevant code.
7. The reranker improves the retrieved results.
8. The context builder prepares relevant information.
9. The AI router directs the request to an appropriate analysis agent.
10. The LLM generates a contextual response.

## Future Improvements

- Support for more programming languages.
- More advanced code understanding.
- Improved retrieval and reranking.
- Automated test generation.
- Enhanced security analysis.
- More advanced debugging capabilities.

## Author

**Nova**

Computer Science & Engineering Student  
Interested in Artificial Intelligence, Machine Learning, and AI Agent Development.

---

**Note:** CodeLens is an independent development project. AI-generated code analysis should be reviewed and tested before applying suggested changes.