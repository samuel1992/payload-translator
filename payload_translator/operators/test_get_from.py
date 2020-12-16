import pytest

from .exceptions import InvalidFieldException
from .get_from import GetFrom


def test_get_field_return_expected_value():
    field = 'nice_phrase'
    value = 'something beautiful'
    payload = {
        field: value
    }

    result = GetFrom(field).call(payload)

    assert result == value


def test_get_field_raises_an_invalid_field():
    field = 'nice_phrase'
    value = 'something beautiful'
    payload = {
        field: value
    }

    with pytest.raises(InvalidFieldException):
        assert GetFrom('invalid_field').call(payload)


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

    result = GetFrom(path).call(payload)

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
        assert GetFrom(path).call(payload)


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

    assert GetFrom(path).call(payload) == value
