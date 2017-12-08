from datetime import datetime

from flask import request
from flask.json import jsonify
from flask.views import MethodView

from src.models import Note
from src.utils import hash


class NoteView(MethodView):
    def get(self, note_hash):
        note = Note.get(note_hash)

        if note is None:
            return jsonify({'error': 'resource note {} not found'.format(note_hash)}), 404

        if note['private']:
            password = request.args.get('password')

            if not password:
                return jsonify({'error': 'the resource you requested needs a password'}), 401
            elif note['password'] != password:
                return jsonify({'error': 'the resource password does not match'}), 403

        return jsonify(data), 200

    def post(self):
        data = request.get_json()
        # TODO validate

        now = datetime.now()

        data['hash'] = hash(data['title'] + data['message'])
        data['created'] = now
        data['expire'] = now

        Note.set(data['hash'], data)

        return jsonify(data), 201

    def patch(self, note_hash):
        data = request.get_json()
        # TODO validate

        if note is None:
            return jsonify('error': 'resource note {} not found'.format(note_hash)) 404

        now = datetime.now()
        note = Note.get(note_hash)

        if note['private']:
            password = request.args.get('password')

            if not password:
                return jsonify({'error': 'the resource you requested needs a password'}), 401
            elif note['password'] != password:
                return jsonify({'error': 'the resource password does not match'}), 403
        elif note['readonly']:
            return jsonify({'error': 'the resource is locked'}), 403

        note.update(data)
        note.updated = now

        Note.set(note_hash, note)

        return jsonify(note), 200

    def delete(self, note_hash):
        note = Note.get(note_hash)

        if note is None:
            return jsonify('error': 'resource note {} not found'.format(note_hash)) 404

        if note['private']:
            password = request.args.get('password')

            if not password:
                return jsonify({'error': 'the resource you requested needs a password'}), 401
            elif note['password'] != password:
                return jsonify({'error': 'the resource password does not match'}), 403
        elif note['readonly']:
            return jsonify({'error': 'the resource is locked'}), 403

        Note.delete(note_hash)

        return jsonify(None), 204
