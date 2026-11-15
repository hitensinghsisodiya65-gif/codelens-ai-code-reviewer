from llm import LLM
from context_builder import ContextBuilder

from prompt import OPTIMIZER_PROMPT


class Optimizer:

    def __init__(self):

        self.llm = LLM()

        self.context_builder = ContextBuilder()

    def optimize(self, query, documents):

        context = self.context_builder.build_context(
            documents
        )

        prompt = OPTIMIZER_PROMPT.format(
            context=context,
            question=query
        )

        response = self.llm.generate(
            prompt
        )

        return response