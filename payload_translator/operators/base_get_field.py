from .exceptions import InvalidFieldException

ERROR_INVALID_FIELD = 'The field passed does not exist in the de payload'


class BaseGetField:
    def _get(self, payload, key):
        try:
            return payload[key]
        except KeyError:
            raise InvalidFieldException(ERROR_INVALID_FIELD)
