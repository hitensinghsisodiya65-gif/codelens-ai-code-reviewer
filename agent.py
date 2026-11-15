from router import Router
from memory import Memory

from reviewer import Reviewer
from debugger import Debugger
from optimizer import Optimizer
from security import Security
from assistant import Assistant

from reranker import ReRanker


class Agent:

    def __init__(self):

        self.memory = Memory()

        self.router = Router()

        self.reviewer = Reviewer()

        self.debugger = Debugger()

        self.optimizer = Optimizer()

        self.security = Security()

        self.assistant = Assistant()

        self.reranker = ReRanker()

    def chat(self, query):

        self.memory.add_user_message(
            query
        )

        semantic_search = self.memory.get_semantic_search()

        if semantic_search:

            retrieved_documents = semantic_search.search(
                query
            )

            ranked_documents = self.reranker.rerank(
                query,
                retrieved_documents
            )

        else:

            ranked_documents = []

        task = self.router.route(
            query
        )

        if task == "review":

            response = self.reviewer.review(
                query,
                ranked_documents
            )

        elif task == "debug":

            response = self.debugger.debug(
                query,
                ranked_documents
            )

        elif task == "optimize":

            response = self.optimizer.optimize(
                query,
                ranked_documents
            )

        elif task == "security":

            response = self.security.analyze(
                query,
                ranked_documents
            )

        elif task == "general":

            response = self.assistant.answer(
                query,
                ranked_documents
            )

        else:

            response = "Sorry, I don't understand your request."

        self.memory.add_ai_message(
            response
        )

        return response