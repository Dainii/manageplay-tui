from models.concerns.api import Api

class Session(Api):
    collection = "sessions"

    def __init__(self, json):
        self.name = json["name"]
        self.description = json["description"]

    @classmethod
    def all(cls):
        sessions = []
        results = cls.index()

        for result in results:
            sessions.append(Session(result))

        return sessions 
