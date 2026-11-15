from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP


class CodeChunker:

    def __init__(self):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len,
            separators=[
                "\nclass ",
                "\ndef ",
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            split_chunks = self.text_splitter.split_text(
                document["content"]
            )

            metadata = document["metadata"]

            for index, chunk in enumerate(split_chunks):

                chunks.append(
                    {
                        "path": metadata["path"],
                        "language": metadata["language"],
                        "extension": metadata["extension"],
                        "tree": metadata["tree"],
                        "chunk_id": index,
                        "content": chunk
                    }
                )

        return chunks