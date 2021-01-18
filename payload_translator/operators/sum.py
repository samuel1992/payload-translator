from .get_from import GetFrom

from .exceptions import InvalidNumberException

ERROR_INVALID_NUMBER = ': The value is not a valid number'


class Sum:
    """Operator to sum values got from another dictionary field. It uses the
    `GetFrom` operator to do it.
    :param: fields: the fields to be sum. In case of a value from a nested
    field you must pass a tuple indicating the path for the value (see the
    GetFrom operator). All of it must be a number. In case of a string it will
    try to convert to a float.
    Ex:
    ```
        payloat to get values from:
        payload = {
          'field_a': 20,
          'field_b': {
            'field_c' {
                  'field_d': 10
                }
            }
        }

        Sum('field_a', ('field_b', 'field_c', 'field_d').call(payload)
    ```
    """
    def __init__(self, *fields):
        self.fields = fields

    def call(self, payload):
        result = 0
        for field in self.fields:
            value = GetFrom(field).call(payload)
            try:
                value = float(value)
            except ValueError:
                raise InvalidNumberException(value + ERROR_INVALID_NUMBER)

            result += value

        return result
