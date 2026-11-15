from pathlib import Path
from tree_sitter_language_pack import get_parser


SUPPORTED_LANGUAGES = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".cs": "c_sharp",
    ".go": "go",
    ".rs": "rust",
    ".php": "php",
    ".rb": "ruby",
    ".swift": "swift",
    ".kt": "kotlin",
    ".html": "html",
    ".css": "css",
}


IGNORE_FOLDERS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
}


class ProjectParser:

    def __init__(self):
        self.parsers = {}

        for language in set(SUPPORTED_LANGUAGES.values()):
            try:
                self.parsers[language] = get_parser(language)
            except Exception:
                pass

    def parse_project(self, project_path):

        documents = []

        project_path = Path(project_path)

        for file_path in project_path.rglob("*"):

            if not file_path.is_file():
                continue

            if any(folder in file_path.parts for folder in IGNORE_FOLDERS):
                continue

            extension = file_path.suffix.lower()

            if extension not in SUPPORTED_LANGUAGES:
                continue

            language = SUPPORTED_LANGUAGES[extension]

            try:

                code = file_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                parser = self.parsers.get(language)

                tree = None

                if parser:
                    tree = parser.parse(
                        bytes(code, "utf-8")
                    )

                documents.append(
                    {
                        "content": code,
                        "metadata": {
                            "path": str(file_path),
                            "language": language,
                            "extension": extension,
                            "tree": tree,
                        },
                    }
                )

            except Exception as e:
                print(f"Skipped {file_path}: {e}")

        return documents