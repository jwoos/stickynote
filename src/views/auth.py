from flask.views import MethodView

from src.models import Auth, Note


class AuthView(MethodView):
    def get(self):
        pass

    def post(self, auth_hash):
        pass

    def delete(self, auth_hash):
        pass


class AuthNoteView(MethodView):
    def get(self, auth_hash, note_hash):
        pass

    def delete(self, auth_hash, note_hash):
        pass

    def patch(self, auth_hash, note_hash):
        pass
