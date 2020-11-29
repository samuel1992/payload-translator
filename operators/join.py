class Join:
    def __init__(self, *operators, delimiter=' '):
        self.operators = operators
        self.delimiter = delimiter

    def call(self, payload):
        values = [str(operator.call(payload)) for operator in self.operators]
        return f'{self.delimiter}'.join(values)
