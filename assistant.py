from llm import LLM
from prompt import GENERAL_PROMPT
from context_builder import ContextBuilder


class Assistant:

    def __init__(self):

        self.llm = LLM()

        self.context_builder = ContextBuilder()

    def answer(self, query, documents):

        context = self.context_builder.build_context(
            documents
        )

        prompt = GENERAL_PROMPT.format(
            context=context,
            question=query
        )

        response = self.llm.invoke(
            prompt
        )

        return response.content