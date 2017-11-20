from flask import Flask
from flask.json import jsonify

import views


app = Flask(__name__)


note_view = views.NoteView.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
app.add_url_rule('/users/<str:note_hash>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])
