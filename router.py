class Router:

    def route(self, query):

        query = query.lower()

        if any(word in query for word in [
            "review",
            "analyze",
            "code review"
        ]):
            return "review"

        elif any(word in query for word in [
            "bug",
            "debug",
            "fix",
            "error"
        ]):
            return "debug"

        elif any(word in query for word in [
            "optimize",
            "performance",
            "faster",
            "efficient"
        ]):
            return "optimize"

        elif any(word in query for word in [
            "security",
            "vulnerability",
            "secure"
        ]):
            return "security"

        else:
            return "general"