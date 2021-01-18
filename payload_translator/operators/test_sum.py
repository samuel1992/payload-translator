import pytest

from .sum import Sum

from .exceptions import InvalidNumberException


def test_sum_a_single_field():
    a = 10

    payload = {
        'a': a
    }

    assert Sum('a').call(payload) == a


def test_sum_multiple_fields():
    a = 10
    b = 11.3
    c = 34.1
    expected_sum = sum([a, b, c])

    payload = {
        'a': a,
        'b': b,
        'c': {
            'd': c
        }
    }

    assert Sum('a', 'b', ('c', 'd')).call(payload) == expected_sum


def test_sum_multiple_fields_with_a_number_in_a_string():
    a = '10'
    b = 11.3
    c = 34.1
    expected_sum = sum([float(a), b, c])

    payload = {
        'a': a,
        'b': b,
        'c': {
            'd': c
        }
    }

    assert Sum('a', 'b', ('c', 'd')).call(payload) == expected_sum


def test_sum_with_a_not_number_value():
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
        assert Sum('a', 'b', ('c', 'd')).call(payload)
