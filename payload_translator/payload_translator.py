from .operators import Operator


class PayloadTranslator:
    def __init__(self, _from, _to):
        self.payload = _from
        self.mapping = _to

    def translate(self):
        return self._resolve_operators(self.mapping)

    def _resolve_operators(self, data):
        if self._is_a_operator(data):
            data = data.call(self.payload)
        else:
            for key, value in data.items():
                if self._is_a_operator(value):
                    data[key] = value.call(self.payload)
                elif isinstance(value, dict):
                    self._resolve_operators(value)
                elif isinstance(value, list):
                    for i, v in enumerate(value):
                        value[i] = self._resolve_operators(v)

        return data

    def _is_a_operator(self, value):
        return issubclass(value.__class__, Operator)
