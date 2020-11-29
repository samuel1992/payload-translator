import pytest

from .get_sub_field import GetSubField
from .exceptions import InvalidFieldException


def test_get_sub_field_return_expected_value():
    value = 'something'
    payload = {
        'first': {
            'second': {
                'third': value
            }
        }
    }

    path = ('first', 'second', 'third')

    result = GetSubField(path).call(payload)

    assert result == value


def test_get_sub_field_raises_an_invalid_field():
    value = 'something'
    payload = {
        'first': {
            'second': {
                'third': value
            }
        }
    }

    path = ('first', 'second', 'invalid')

    with pytest.raises(InvalidFieldException):
        assert GetSubField(path).call(payload)


def test_get_sub_field_with_a_more_level_than_exists():
    value = 'something'
    payload = {
        'first': {
            'second': {
                'third': value
            }
        }
    }

    path = ('first', 'second', 'third', 'forth')

    assert GetSubField(path).call(payload) == value
