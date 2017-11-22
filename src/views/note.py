from flask import request
from flask.json import jsonify
from flask.views import MethodView

from src.models import Note
from src.utils import dict_decode, dict_encode, hash


class NoteView(MethodView):
    def get(self, note_hash):
        raw_data = Note.get(note_hash)

        if raw_data is None:
            return jsonify({'error': '%s not found'.format(note_hash)}), 404

        data = dict_decode(Note.schema, raw_data)
        return jsonify(data), 200

    def post(self):
        data = request.get_json()
        raw_data = dict_decode(Note.schema, data)
        h = hash(data['title'] + data['message'])
        Note.set(h, raw_data)
        return jsonify(data), 201

    def delete(self, hash):
        pass
