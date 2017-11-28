from datetime import datetime

from src.models.common import BaseModel


class Note(BaseModel):
    key = 'note:{hash}'

    schema = {
        'hash': (None, None),
        'title': (None, None),
        'message': (None, None),
        'password': (None, None),
        'access': (None, None),
        'editable': (None, None),
        'private': (None, None),
        'created': BaseModel.compose_de_serializer([datetime.timestamp], [float, datetime.fromtimestamp]),
        'updated': BaseModel.compose_de_serializer([datetime.timestamp], [float, datetime.fromtimestamp]),
        'expire': BaseModel.compose_de_serializer([datetime.timestamp], [float, datetime.fromtimestamp])
    }

    validation_schema = {

    }

    def __init__(self, title=None, message=None, views=None, created=None, expire=None, hash=None):
        self.hash = hash

        self.title = title
        self.message = message

        self.password = password
        self.access = access
        self.editable = editable
        self.private = private

        self.created = created
        self.updated = updated
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
            'password': '',
            'access': '',
            'editable': '',
            'private': '',
            'created': '',
            'updated': '',
            'expire': ''
        }
