from .exceptions import InvalidFieldException

from .operator import Operator

ERROR_INVALID_FIELD = ': The field does not exist in the de payload'


class GetFrom(Operator):
    """Operator to get values from another dictonary directly or in a
    sublevel when it is a nested field.
    :param: field: a string for the field that you want the value or a tuple
    of string representing the path to find a value in a nested field.
    """
    def __init__(self, field):
        self.field = field

    def _get(self, payload, key):
        try:
            return payload[key]
        except KeyError:
            raise InvalidFieldException(key + ERROR_INVALID_FIELD)

    def _get_from_nested_field(self, payload):
        path = self.field
        for key in path:
            value = self._get(payload, key)
            if not isinstance(value, dict):
                return value
            payload = value

        return payload

    def call(self, payload):
        if isinstance(self.field, tuple):
            return self._get_from_nested_field(payload)

        return self._get(payload, self.field)
