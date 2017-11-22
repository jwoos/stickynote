from abc import ABC

from src.store import redis_client
from src.utils import compose


class BaseModel(ABC):
    DEFAULT_DE_SERIALIZER = ([str, str.encode], [bytes.decode])
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

    @staticmethod
    def dict_encode(data):
        raw_data = {}

        for k, v in data.items():
            raw_data[k.encode()] = v

        return raw_data

    @staticmethod
    def dict_decode(raw_data):
        data = {}

        for k, v in raw_data.items():
            data[k.decode()] = v

        return data

    @classmethod
    def compose_de_serializer(cls, serializer_fns=[], deserializer_fns=[]):
        serializer, deserializer = cls.DEFAULT_DE_SERIALIZER
        return (compose(*serializer_fns, *serializer), compose(*deserializer, *deserializer_fns))

    @classmethod
    def get(cls, hash):
        return cls.client.hgetall(cls.form_key(hash))

    @classmethod
    def set(cls, hash, data):
        return cls.client.hmset(cls.form_key(hash), data)

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

    def dict_to_model(self, data):
        data = BaseModel.dict_decode(data)

        obj = self

        for k in self.schema['KEY']:
            setattr(obj, k, data[k])

        for k, constructor in self.schema.items():
            _, deserializer = constructor
            if deserializer:
                setattr(obj, k, deserializer(data[k]))
            else:
                setattr(obj, k, data[k])

        return obj

    def model_to_dict(self, model):
        data = {}

        for k, constructor in self.schema.items():
            serializer, _ = constructor
            if serializer is not None:
                data[k] = serializer(getattr(model, k))
            else:
                data[k] = getattr(model, k)

        data = BaseModel.dict_encode(data)
        return data

    def json(self):
        return self.__dict__
