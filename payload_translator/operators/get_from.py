from .exceptions import InvalidFieldException

ERROR_INVALID_FIELD = ': The field does not exist in the de payload'


class GetFrom:
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
        if isinstance(self.field, (list, tuple)):
            return self._get_from_nested_field(payload)

        return self._get(payload, self.field)
