from .base_get_field import BaseGetField


class GetField(BaseGetField):
    def __init__(self, field):
        self.field = field

    def call(self, payload):
        return self._get(payload, self.field)
