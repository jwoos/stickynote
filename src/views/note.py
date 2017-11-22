from flask.views import MethodView

from src.store import redis_client


class NoteView(MethodView):
    def get(self, hash):
        pass

    def post(self):
        pass

    def delete(self, hash):
        pass
