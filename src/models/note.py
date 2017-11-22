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
    def form_key(hash):
        return Note.key.format(hash=hash)

    @staticmethod
    def get(hash):
        return Note.client.hmget(Note.form_key(hash))

    @staticmethod
    def set(hash, data):
        return Note.client.hmset(Note.form_key(hash), data)

    @staticmethod
    def delete(hash):
        return Note.client.delete(Note.form_key(hash))

    @staticmethod
    def patch(hash, data):
        pass

    @staticmethod
    def keys(hash):
        return Note.client.hkeys(hash)

    @staticmethod
    def get_key(hash, key):
        return Note.client.hget(Note.form_key(hash))

    @staticmethod
    def set_key(hash, key, data):
        return Note.client.hset(Note.form_key(hash), key, data)

    @staticmethod
    def delete_key(hash, key):
        return Note.client.hdel(Note.form_key(hash), key)
