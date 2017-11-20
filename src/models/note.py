from src.models.common import BaseModel

from src.store import redis_client


class Note(BaseModel):
    key = 'note:{hash}'
    client = redis_client

    def __init__(self, title=None, message=None, views=None, created=None, expire=None, hash=None):
        self.hash = hash

        self.title = title
        self.message = message

        self.views = views

        self.created = created
        self.expire = expire

    @staticmethod
    def form_key(self, hash):
        return self.key.format(hash=hash)

    @staticmethod
    def get(self, hash):
        self.client.get('')

    @staticmethod
    def set(self, hash, data):
        pass

    @staticmethod
    def delete(self, hash):
        pass

    @staticmethod
    def patch(self, hash, data):
        pass
