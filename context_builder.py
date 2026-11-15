from typing import List, Dict


class ContextBuilder:

    def __init__(self):
        pass

    def build_context(self, documents: List[Dict]) -> str:

        if not documents:
            return "No relevant code was found."

        context = []

        for index, document in enumerate(documents, start=1):

            metadata = document["metadata"]

            file_path = metadata.get("path", "Unknown")

            language = metadata.get("language", "Unknown")

            chunk_id = metadata.get("chunk_id", "Unknown")

            code = document["content"]

            context.append(
                f"""
==============================
Document {index}

File: {file_path}
Language: {language}
Chunk ID: {chunk_id}

Code:
{code}
==============================
"""
            )

        return "\n".join(context)