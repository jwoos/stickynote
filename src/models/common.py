from abc import ABC


class BaseModel(ABC):
    def json(self):
        return self.__dict__
