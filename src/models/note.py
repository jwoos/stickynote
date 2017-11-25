from datetime import datetime

from src.models.common import BaseModel


class Note(BaseModel):
    key = 'note:{hash}'
    schema = {
        'hash': (None, None),
        'title': (None, None),
        'message': (None, None),
        'created': BaseModel.compose_de_serializer([datetime.timestamp], [float, datetime.fromtimestamp]),
        'expire': BaseModel.compose_de_serializer([datetime.timestamp], [float, datetime.fromtimestamp])
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

    @staticmethod
    def init_base():
        return {
            'hash': '',
            'title': '',
            'message': '',
            'created': '',
            'expire': ''
        }
