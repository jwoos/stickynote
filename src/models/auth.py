from datetime import datetime

from src.models.common import BaseModel


class Auth(BaseModel):
    key = 'auth:{hash}'
    schema = {
        'hash': (None, None),
        'password': (None, None),
        'notes': ([lambda x: '-'.join(x)], [lambda x: x.split('-')]),
        'created': ([datetime.timestamp], [datetime.fromtimestamp]),
        'expire': ([datetime.timestamp], [datetime.fromtimestamp])
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

    @staticmethod
    def init_base():
        return {
            'hash': '',
            'title': '',
            'notes': '',
            'created': '',
            'expire': ''
        }
