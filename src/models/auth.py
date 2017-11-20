class AuthModel:
    def __init__(self, hash=None):
        self.hash = hash


class Auth:
    key = 'auth:{hash}'

    def __init__(self, client):
        self.client = client
