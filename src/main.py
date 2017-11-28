from flask import Flask
from flask.json import jsonify

import src.views as views


app = Flask(__name__)


note_view = views.note.NoteView.as_view('note')
app.add_url_rule('/note', view_func=note_view, methods=['POST'])
app.add_url_rule('/note/<string:note_hash>', view_func=note_view, methods=['GET', 'DELETE'])
