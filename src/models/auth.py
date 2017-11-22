from datetime import datetime

from src.models.common import BaseModel


class Auth(BaseModel):
    key = 'auth:{hash}'
    schema = {
        'hash': BaseModel.compose_de_serializer(DEFAULT_DE_SERIALIZER),
        'password': BaseModel.compose_de_serializer(DEFAULT_DE_SERIALIZER),
        'notes': ([lambda x: '-'.join(x), str.encode], [bytes.decode, lambda x: x.split('-')]),
        'created': ([datetime.timestamp, str, str.encode], [bytes.decode, datetime.fromtimestamp])
        'expire': ([datetime.timestamp, str, str.encode], [bytes.decode, datetime.fromtimestamp])
    }

    def __init__(self, password=None, notes=None, created=None, expire=None, hash=None):
        self.hash = hash

        self.password = password

        self.notes = notes

        self.created = created
        self.expire = expire

    @staticmethod
    def form_key(hash):
        return Auth.key.format(hash=hash)
