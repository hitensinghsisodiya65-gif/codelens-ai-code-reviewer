from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME


class Reply(str):
    """Plain text that also has a .content attribute, so every agent works
    whether it treats the answer as text or as a LangChain message."""

    @property
    def content(self):
        return str(self)


class _LLM:

    def __init__(self):
        self.model = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0.2,
        )

    def _ask(self, prompt):
        result = self.model.invoke(prompt)
        text = result if isinstance(result, str) else getattr(result, "content", str(result))
        return Reply(text)

    def invoke(self, prompt):      # used by Assistant
        return self._ask(prompt)

    def generate(self, prompt):    # used by Reviewer, Debugger, Optimizer, Security
        return self._ask(prompt)


def LLM():
    return _LLM()
