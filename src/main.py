from flask import Flask
from flask.json import jsonify


app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'a': 1, 'b': 2})
