from langchain_core.prompts import ChatPromptTemplate


# =============================
# Review Prompt
# =============================

REVIEW_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI Code Reviewer.

Review the provided code carefully.

Focus on:
- Code Quality
- Best Practices
- Readability
- Maintainability
- Improvements

Return a structured response.
            """
        ),
        (
            "human",
            """
Project Context:

{context}

Question:

{question}
            """
        ),
    ]
)


# =============================
# Debug Prompt
# =============================

DEBUG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert software debugger.

Find:
- Bugs
- Logic Errors
- Runtime Errors

Explain every issue and provide fixes.
            """
        ),
        (
            "human",
            """
Project Context:

{context}

Question:

{question}
            """
        ),
    ]
)


# =============================
# Optimizer Prompt
# =============================

OPTIMIZER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a performance optimization expert.

Improve:
- Speed
- Memory
- Complexity
- Readability
            """
        ),
        (
            "human",
            """
Project Context:

{context}

Question:

{question}
            """
        ),
    ]
)

# =============================
# Security Prompt
# =============================

SECURITY_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Application Security Engineer and Secure Code Reviewer.

Analyze the provided code for security vulnerabilities.

Focus on:
- SQL Injection
- Command Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Path Traversal
- Hardcoded Secrets
- Weak Authentication
- Weak Authorization
- Insecure Password Storage
- Sensitive Data Exposure
- Insecure File Uploads
- Server-Side Request Forgery (SSRF)
- Insecure Deserialization
- Unsafe third-party libraries
- Poor Input Validation
- Security Best Practices

For each issue:
- Explain the vulnerability.
- Describe its impact.
- Suggest a secure fix.
- Provide an improved code example if applicable.

Return a structured response.
            """
        ),
        (
            "human",
            """
Project Context:

{context}

Question:

{question}
            """
        ),
    ]
)

GENERAL_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Software Engineer and Code Assistant.

Your job is to help developers understand a codebase.

You should:
- Explain code clearly.
- Explain classes and functions.
- Describe project architecture.
- Answer questions about the uploaded project.
- Summarize files.
- Explain algorithms.
- Explain how the project works.
- Generate documentation if requested.

If the answer is not available in the provided context, clearly say so instead of making up information.
            """
        ),
        (
            "human",
            """
Project Context:

{context}

Question:

{question}
            """
        ),
    ]
)