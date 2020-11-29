from .join import Join
from .get_field import GetField
from .get_sub_field import GetSubField


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

    result = Join(GetField('name'),
                  GetField('last_name'),
                  GetSubField(('birthday', 'month')),
                  GetSubField(('birthday', 'day'))).call(payload)

    assert result == f'{name} {last_name} {month} {day}'

