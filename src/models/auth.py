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
    def form_key(hash):
        return Auth.key.format(hash=hash)

    @staticmethod
    def get(hash):
        return Auth.client.hmget(Auth.form_key(hash))

    @staticmethod
    def set(hash, data):
        return Auth.client.hmset(Auth.form_key(hash), data)

    @staticmethod
    def delete(hash):
        return Auth.client.delete(Auth.form_key(hash))

    @staticmethod
    def patch(hash, data):
        pass

    @staticmethod
    def keys(hash):
        return Auth.client.hkeys(hash)

    @staticmethod
    def get_key(hash, key):
        return Auth.client.hget(Auth.form_key(hash))

    @staticmethod
    def set_key(hash, key, data):
        return Auth.client.hset(Auth.form_key(hash), key, data)

    @staticmethod
    def delete_key(hash, key):
        return Auth.client.hdel(Auth.form_key(hash), key)
