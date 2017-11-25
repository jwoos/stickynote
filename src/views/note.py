from datetime import datetime

from flask import request
from flask.json import jsonify
from flask.views import MethodView

from src.models import Note
from src.utils import hash


class NoteView(MethodView):
    def get(self, note_hash):
        data = Note.get(note_hash)

        if data is None:
            return jsonify({'error': '%s not found'.format(note_hash)}), 404

        return jsonify(data), 200

    def post(self):
        data = Note.init_base()
        request_data = request.get_json()
        # TODO validate
        data.update(request_data)
        data['hash'] = hash(data['title'] + data['message'])
        data['created'] = datetime.now()
        data['expire'] = datetime.now()
        Note.set(data['hash'], data)
        return jsonify(data), 201

    def delete(self, hash):
        pass
