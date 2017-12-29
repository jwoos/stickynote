from datetime import datetime

from flask import request
from flask.json import jsonify
from flask.views import MethodView

from src.errors import NotFoundError, UnauthorizedError, ForbiddenError, ValidationError
from src.models.note import Note, note_post_schema, note_patch_schema
from src.utils import hash
from src.validator import validate_data


class NoteView(MethodView):
    def get(self, note_hash):
        note = Note.get(note_hash)

        if note is None:
            raise NotFoundError('the resource does not exist')

        if note['private']:
            password = request.args.get('password')

            if not password:
                raise UnauthorizedError('the resource needs a password')
            elif note['password'] != password:
                raise ForbiddenError('the resource password does not match')

        return jsonify(note), 200

    def post(self):
        data = request.get_json()

        if not data:
            raise ValidationError('data cannot be empty')

        validate_data(note_post_schema, data, strict=True)

        now = int(datetime.now().timestamp())

        data['hash'] = hash(data['title'] + data['message'])
        data['created'] = now

        Note.set(data['hash'], data)

        if 'expire' in data:
            Note.expire_at(data['hash'], data['expire'])

        return jsonify(Note.get(data['hash'])), 201

    def patch(self, note_hash):
        data = request.get_json()

        validate_data(note_patch_schema, data, strict=True)

        now = int(datetime.now().timestamp())

        note = Note.get(note_hash)

        if note is None:
            raise NotFoundError('the resource does not exist')

        if note['private']:
            password = request.args.get('password')

            if not password:
                raise UnauthorizedError('the resource needs a password')
            elif note['password'] != password:
                raise ForbiddenError('the resource password does not match')
        elif note['readonly']:
            raise ForbiddenError('the resource is locked')

        note.update(data)
        note['updated'] = now

        Note.set(note_hash, note)

        if 'expire' in note:
            Note.expire_at(note['hash'], note['expire'])

        return jsonify(note), 200

    def delete(self, note_hash):
        note = Note.get(note_hash)

        if note is None:
            raise NotFoundError('the resource does not exist')

        if note['private']:
            password = request.args.get('password')

            if not password:
                raise UnauthorizedError('the resource needs a password')
            elif note['password'] != password:
                raise ForbiddenError('the resource password does not match')
        elif note['readonly']:
            raise ForbiddenError('the resource is locked')

        Note.delete(note_hash)

        return jsonify(None), 204
