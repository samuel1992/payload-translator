from .operator import Operator


class Join(Operator):
    """Operator to join values got from another operators. It join them into a
    string with the values obtained.
    :param: operators: the operators object to get the values
    :param: delimiter: the delimiter character to put in the final string with
    the joined values
    """
    def __init__(self, *operators, delimiter=' '):
        self.operators = operators
        self.delimiter = delimiter

    def call(self, payload):
        values = [str(operator.call(payload)) for operator in self.operators]
        return f'{self.delimiter}'.join(values)
