class PayloadTranslator:
    def __init__(self, _from, _to):
        self.payload = _from
        self.mapping = _to

    def translate(self):
        translated_payload = {}

        for key, operator in self.mapping.items():
            translated_payload[key] = operator.call(self.payload)

        return translated_payload
