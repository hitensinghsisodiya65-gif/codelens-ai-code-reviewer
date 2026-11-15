from llm import LLM
from context_builder import ContextBuilder

from prompt import SECURITY_PROMPT


class Security:

    def __init__(self):

        self.llm = LLM()

        self.context_builder = ContextBuilder()

    def analyze(self, query, documents):

        context = self.context_builder.build_context(
            documents
        )

        prompt = SECURITY_PROMPT.format(
            context=context,
            question=query
        )

        response = self.llm.generate(
            prompt
        )

        return response