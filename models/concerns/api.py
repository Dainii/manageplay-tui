import requests

class Api():
    collection = ""
    headers = {"accept":"application/json"}

    @classmethod
    def index(cls):
        return requests.get(f"http://127.0.0.1:3000/{cls.collection}", headers=cls.headers).json()

    @classmethod
    def show(cls, id):
        return requests.get(f"http://127.0.0.1:3000/{cls.collection}/{id}", headers=cls.headers).json()
