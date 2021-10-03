from .join import Join


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

    result = Join('name', 'last_name',
                  ('birthday', 'month'), ('birthday', 'day')).call(payload)

    assert result == f'{name} {last_name} {month} {day}'
