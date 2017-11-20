from flask.views import MethodView

from src.store import redis_client


class NoteView(MethodView):
    def get(self):
        pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


class NotesView(MethodView):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
