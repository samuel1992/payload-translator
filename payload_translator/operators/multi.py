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

        Multi('field_a', ('field_b', 'field_c', 'field_d').call(payload)
    ```
    """
    def __init__(self, *fields):
        self.fields = fields

    def call(self, payload):
        first_value = GetFrom(self.fields[0]).call(payload)
        try:
            result = float(first_value)
        except ValueError:
            raise InvalidNumberException(first_value + ERROR_INVALID_NUMBER)

        for field in self.fields[1::]:
            value = GetFrom(field).call(payload)
            try:
                value = float(value)
            except ValueError:
                raise InvalidNumberException(value + ERROR_INVALID_NUMBER)

            result *= value

        return result
