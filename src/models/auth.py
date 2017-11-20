from src.models.common import BaseModel

from src.store import redis_client


class Auth(BaseModel):
    key = 'auth:{hash}'
    client = redis_client

    def __init__(self, password=None, notes=None, created=None, expire=None, hash=None):
        self.hash = hash

        self.password = password

        self.notes = notes

        self.created = created
        self.expire = expire

    @staticmethod
    def form_key(self, hash):
        return self.key.format(hash=hash)

    @staticmethod
    def get(self, hash):
        pass

    @staticmethod
    def set(self, hash, data):
        pass

    @staticmethod
    def delete(self, hash):
        pass

    @staticmethod
    def patch(self, hash, data):
        pass
