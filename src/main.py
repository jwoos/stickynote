from flask import Flask
from flask.json import jsonify

import views


app = Flask(__name__)


note_view = views.NoteView.as_view('note')
app.add_url_rule('/note/', view_func=note_view, methods=['POST'])
app.add_url_rule('/note/<str:note_hash>', view_func=note_view, methods=['GET', 'PATCH', 'DELETE'])

auth_view = views.NoteView.as_view('auth')

