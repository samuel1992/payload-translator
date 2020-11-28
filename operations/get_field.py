ERROR_INVALID_FIELD = 'The field passed does not exist in the de payload'


class InvalidFieldException(Exception):
    pass


class GetField:
    def __init__(self, field):
        self.field = field

    def call(self, payload):
        try:
            return payload[self.field]
        except KeyError:
            raise InvalidFieldException(ERROR_INVALID_FIELD)
