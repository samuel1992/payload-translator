from .operator import Operator

from .get_from import GetFrom


class Join(Operator):
    """Operator to join values got from another operators. It join them into a
    string with the values obtained.
    :param: operators: the operators object to get the values
    :param: delimiter: the delimiter character to put in the final string with
    the joined values
    """
    def __init__(self, *fields, delimiter=' '):
        self.fields = fields
        self.delimiter = delimiter

    def call(self, payload):
        values = [str(GetFrom(field).call(payload)) for field in self.fields]
        return f'{self.delimiter}'.join(values)
