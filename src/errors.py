import abc

from werkzeug.exceptions import *


class BaseError(Exception, abc.ABC):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    @abc.abstractmethod
    def form_json(self):
        raise NotImplementedError()


class BaseAPIError(HTTPException):
    def get_description(self, _=None):
        return self.description

    def get_body(self, _=None):
        return {
            'error': {
                'code': self.code,
                'description': self.description
            }
        }

    def get_headers(self, _=None):
        return [('Content-Type', 'application/json')]


class ValidationError(BaseAPIError, UnprocessableEntity):
    pass


class NotFoundError(BaseAPIError, NotFound):
    pass


class UnauthorizedError(BaseAPIError, Unauthorized):
    pass


class ForbiddenError(BaseAPIError, Forbidden):
    pass
