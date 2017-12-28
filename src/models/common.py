from abc import ABC, abstractmethod

from src.store import redis_client
from src.utils import compose, dict_encode, dict_decode


class BaseModel(ABC):
    # (serializer, deserializer)
    key = None
    client = redis_client
    schema = {}

    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def form_key(hash):
        raise NotImplementedError()

    @classmethod
    def compose_de_serializer(cls, serializer_fns=[], deserializer_fns=[]):
        return (compose(*serializer_fns), compose(*deserializer_fns))

    @classmethod
    def get(cls, hash):
        data = cls.init_base()
        raw_data = cls.client.hgetall(cls.form_key(hash))
        _data = dict_decode(cls.schema, raw_data)
        data.update(_data)
        return data

    @classmethod
    def set(cls, hash, data):
        _data = cls.init_base()
        _data.update(data)
        data = _data
        raw_data = dict_encode(cls.schema, data)
        return cls.client.hmset(cls.form_key(hash), raw_data)

    @classmethod
    def delete(cls, hash):
        return cls.client.delete(cls.form_key(hash))

    @classmethod
    def keys(cls, hash):
        return cls.client.hkeys(hash)

    @classmethod
    def values(cls, hash):
        return cls.client.hvals(hash)

    @classmethod
    def get_key(cls, hash, key):
        return cls.client.hget(cls.form_key(hash))

    @classmethod
    def set_key(cls, hash, key, data):
        return cls.client.hset(cls.form_key(hash), key, data)

    @classmethod
    def delete_key(cls, hash, key):
        return cls.client.hdel(cls.form_key(hash), key)

    def json(self):
        return self.__dict__
