from .base_get_field import BaseGetField


class GetSubField(BaseGetField):
    def __init__(self, path):
        self.path = path

    def call(self, payload):
        for key in self.path:
            value = self._get(payload, key)
            if not isinstance(value, dict):
                return value

            payload = value
