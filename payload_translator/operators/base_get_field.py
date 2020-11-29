from .exceptions import InvalidFieldException

ERROR_INVALID_FIELD = ': The field does not exist in the de payload'


class BaseGetField:
    def _get(self, payload, key):
        try:
            return payload[key]
        except KeyError:
            raise InvalidFieldException(key + ERROR_INVALID_FIELD)
