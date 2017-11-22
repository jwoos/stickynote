from flask import Flask
from flask.json import jsonify

import src.views as views


app = Flask(__name__)


note_view = views.note.NoteView.as_view('note')
app.add_url_rule('/note', view_func=note_view, methods=['POST'])
app.add_url_rule('/note/<string:note_hash>', view_func=note_view, methods=['GET', 'DELETE'])

auth_view = views.auth.AuthView.as_view('auth')
app.add_url_rule('/auth/', view_func=auth_view, methods=['POST'])
app.add_url_rule('/auth/<string:auth_hash>', view_func=auth_view, methods=['GET', 'DELETE'])

auth_note_view = views.auth.AuthNoteView.as_view('auth_note')
app.add_url_rule('/auth/<string:auth_hash>/note', view_func=auth_note_view, methods=['GET', 'DELETE'])
app.add_url_rule('/auth/<string:auth_hash>/note/<string:note_hash>', view_func=auth_note_view, methods=['GET', 'PATCH', 'DELETE'])
