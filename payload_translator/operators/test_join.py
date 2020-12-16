from .join import Join

from .get_from import GetFrom


def test_join_fields_values():
    name = 'samuel'
    last_name = 'dantas'
    month = 'October'
    day = 27

    payload = {
        'name': name,
        'last_name': last_name,
        'birthday': {
            'month': month,
            'day': day
        }
    }

    result = Join(GetFrom('name'),
                  GetFrom('last_name'),
                  GetFrom(('birthday', 'month')),
                  GetFrom(('birthday', 'day'))).call(payload)

    assert result == f'{name} {last_name} {month} {day}'
