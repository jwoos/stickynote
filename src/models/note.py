class NoteModel:
    def __init__(self, title, message, hash=None):
        self.title = title
        self.message = message
        self.hash = hash


class Note:
    key = 'note:{hash}'

    def __init__(self, client):
        self.client = client

    def get(self, hash):
        self.client.get('')

    def post(self):
        pass
