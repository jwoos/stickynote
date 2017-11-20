from flask.views import MethodView

from src.store import redis_client


class AuthView(MethodView):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
