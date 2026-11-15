from langchain_core.messages import HumanMessage, AIMessage


class Memory:

    def __init__(self):

        self.messages = []

        self.project_path = None

        self.semantic_search = None

    def set_project(self, project_path):

        self.project_path = project_path

    def get_project(self):

        return self.project_path

    def set_semantic_search(self, semantic_search):

        self.semantic_search = semantic_search

    def get_semantic_search(self):

        return self.semantic_search

    def add_user_message(self, message):

        self.messages.append(
            HumanMessage(content=message)
        )

    def add_ai_message(self, message):

        self.messages.append(
            AIMessage(content=message)
        )

    def get_messages(self):

        return self.messages

    def clear(self):

        self.messages = []

        self.project_path = None

        self.semantic_search = None