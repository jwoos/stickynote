from datetime import datetime

from src.models.common import BaseModel


note_post_schema = {
    'title': {
        'type': 'string',
        'required': False,
        'nullable': True
    },
    'message': {
        'type': 'string',
        'required': True,
        'nullable': True
    },
    'password': {
        'type': 'string',
        'required': False,
        'nullable': False
    },
    'readonly': {
        'type': 'boolean',
        'required': False,
        'nullable': False
    },
    'private': {
        'type': 'boolean',
        'required': False,
        'nullable': False
    },
    'expire': {
        'type': 'integer',
        'required': False,
        'nullable': False
    }
}

note_patch_schema = {
    'title': {
        'type': 'string',
        'required': False,
        'nullable': False
    },
    'message': {
        'type': 'string',
        'required': False,
        'nullable': False
    },
    'password': {
        'type': 'string',
        'required': False,
        'nullable': False
    },
    'readonly': {
        'type': 'boolean',
        'required': False,
        'nullable': False
    },
    'private': {
        'type': 'boolean',
        'required': False,
        'nullable': False
    },
    'expire': {
        'type': 'integer',
        'required': False,
        'nullable': False
    }
}


class Note(BaseModel):
    key = 'note:{hash}'

    schema = {
        'hash': (None, None),
        'title': (None, None),
        'message': (None, None),
        'password': (None, None),
        'readonly': BaseModel.compose_de_serializer([int], [int, bool]),
        'private': BaseModel.compose_de_serializer([int], [int, bool]),
        'created': BaseModel.compose_de_serializer([int], [int]),
        'updated': BaseModel.compose_de_serializer([int], [int]),
        'expire': BaseModel.compose_de_serializer([int], [int])
    }

    validation_schema = {

    }

    def __init__(self, title=None, message=None, views=None, created=None, expire=None, hash=None):
        self.hash = hash

        self.title = title
        self.message = message

        self.password = password
        self.readonly = readonly
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
            'readonly': False,
            'private': False,
            'created': None,
            'updated': None,
            'expire': None
        }
