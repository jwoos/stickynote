from datetime import datetime

from src.models.common import BaseModel


class Note(BaseModel):
    key = 'note:{hash}'
    schema = {
        'hash': BaseModel.compose_de_serializer(DEFAULT_DE_SERIALIZER),
        'title': BaseModel.compose_de_serializer(DEFAULT_DE_SERIALIZER),
        'message': BaseModel.compose_de_serializer(DEFAULT_DE_SERIALIZER),
        'created': ([datetime.timestamp, str, str.encode], [bytes.decode, datetime.fromtimestamp])
        'expire': ([datetime.timestamp, str, str.encode], [bytes.decode, datetime.fromtimestamp])
    }

    def __init__(self, title=None, message=None, views=None, created=None, expire=None, hash=None):
        self.hash = hash

        self.title = title
        self.message = message

        self.created = created
        self.expire = expire

    @classmethod
    def form_key(cls, hash):
        return cls.key.format(hash=hash)
