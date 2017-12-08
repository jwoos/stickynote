from flask import Flask
from flask.json import jsonify
from werkzeug.exceptions import HTTPException, default_exceptions

from src.errors import BaseAPIError, ValidationError, NotFoundError, UnauthorizedError, ForbiddenError
import src.views as views


app = Flask(__name__)


def default_error_handler(error):
    try:
        context = jsonify(error.get_body())
        code = error.code
    except:
        context = jsonify({
            'error': {
                'description': getattr(error, 'message') or getattr(error, 'description') or str(error),
                'code': getattr(error, 'status_code') or getattr(error, 'code') or 500
            }
        })

    return context, code

for code, error in default_exceptions.items():
    app.register_error_handler(error, default_error_handler)

note_view = views.note.NoteView.as_view('note')
app.add_url_rule('/notes', view_func=note_view, methods=['POST'])
app.add_url_rule('/notes/<string:note_hash>', view_func=note_view, methods=['GET', 'PATCH', 'DELETE'])
