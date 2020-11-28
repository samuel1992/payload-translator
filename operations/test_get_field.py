import pytest

from .get_field import GetField, InvalidFieldException


def test_get_field_return_expected_value():
    field = 'nice_phrase'
    value = 'something beautiful'
    payload = {
        field: value
    }

    result = GetField(field).call(payload)

    assert result == value


def test_get_field_does_not_return_expected_value():
    field = 'nice_phrase'
    value = 'something beautiful'
    payload = {
        field: value
    }

    with pytest.raises(InvalidFieldException):
        assert GetField('invalid_field').call(payload)
