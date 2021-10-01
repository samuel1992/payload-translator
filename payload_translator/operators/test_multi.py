import pytest

from .multi import Multi, InvalidNumberException


def test_multiply_field_values():
    a = 1
    b = 2
    c = 3

    payload = {
        'a': a,
        'b': b,
        'c': c
    }

    result = Multi('a', 'b', 'c').call(payload)
    expected_result = a * b * c

    assert result == expected_result


def test_multiply_raises_an_invalid_number_error():
    a = 1
    b = 2
    c = 'not a number'

    payload = {
        'a': a,
        'b': b,
        'c': c
    }

    with pytest.raises(InvalidNumberException):
        assert Multi('a', 'b', 'c').call(payload)
