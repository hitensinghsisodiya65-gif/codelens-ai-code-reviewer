from llm import LLM
from context_builder import ContextBuilder

from prompt import DEBUG_PROMPT


class Debugger:

    def __init__(self):

        self.llm = LLM()

        self.context_builder = ContextBuilder()

    def debug(self, query, documents):

        context = self.context_builder.build_context(
            documents
        )

        prompt = DEBUG_PROMPT.format(
            context=context,
            question=query
        )

        response = self.llm.generate(
            prompt
        )

        return response