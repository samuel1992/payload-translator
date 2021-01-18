import pytest

from .sub import Sub

from .exceptions import InvalidNumberException


def test_sub_a_single_value():
    a = 10

    payload = {
        'a': a
    }

    assert Sub('a').call(payload) == a


def test_sub_multiple_values():
    a = 10
    b = 2
    c = 1
    expected_sub = a - b - c

    payload = {
        'a': a,
        'b': b,
        'c': {
            'd': c
        }
    }

    assert Sub('a', 'b', ('c', 'd')).call(payload) == expected_sub


def test_sub_multiple_values_with_first_number_inside_a_string():
    a = '10'
    b = 2
    c = 1
    expected_sub = float(a) - b - c

    payload = {
        'a': a,
        'b': b,
        'c': {
            'd': c
        }
    }

    assert Sub('a', 'b', ('c', 'd')).call(payload) == expected_sub


def test_sub_multiple_values_with_a_number_inside_a_string():
    a = 10
    b = '2'
    c = 1
    expected_sub = a - float(b) - c

    payload = {
        'a': a,
        'b': b,
        'c': {
            'd': c
        }
    }

    assert Sub('a', 'b', ('c', 'd')).call(payload) == expected_sub


def test_sub_with_a_not_number_value():
    a = 'invalid number'
    b = 11.3
    c = 34.1

    payload = {
        'a': a,
        'b': b,
        'c': {
            'd': c
        }
    }

    with pytest.raises(InvalidNumberException):
        assert Sub('a', 'b', ('c', 'd')).call(payload)
