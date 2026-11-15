from llm import LLM
from context_builder import ContextBuilder

from prompt import REVIEW_PROMPT


class Reviewer:

    def __init__(self):

        self.llm = LLM()

        self.context_builder = ContextBuilder()

    def review(self, query, documents):

        context = self.context_builder.build_context(
            documents
        )

        prompt = REVIEW_PROMPT.format(
            context=context,
            question=query
        )

        response = self.llm.generate(
            prompt
        )

        return response