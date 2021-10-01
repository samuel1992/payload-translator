import math

from .get_from import GetFrom

from .operator import Operator

from .exceptions import InvalidNumberException

ERROR_INVALID_NUMBER = ': The value is not a valid number'


class Multi(Operator):
    """Operator to multiply values got from another dictionary field.
    It uses the `GetFrom` operator to do it.
    :param: fields: the fields to be multiplied. In case of a value from a
    nested field you must pass a tuple indicating the path for the value
    (see the GetFrom operator). All of it must be a number.
    In case of a string it will try to convert to a float.
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

        Multi('field_a', 'field_b', 'field_c', 'field_d').call(payload)
    ```
    """
    def __init__(self, *fields):
        self.fields = fields

    def call(self, payload):
        numbers = []
        for field in self.fields:
            number = GetFrom(field).call(payload)
            try:
                numbers.append(float(number))
            except ValueError:
                raise InvalidNumberException(field + ERROR_INVALID_NUMBER)

        return math.prod(numbers)
