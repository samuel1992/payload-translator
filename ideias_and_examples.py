BASE_PAYLOAD = {
    'name': 'Samuel',
    'last_name': 'Dantas',
    'age': 28,
    'address': {
        'street': 'R. Some Fake Street',
        'number': 123,
        'city': 'Osasco',
        'state': 'SP'
    },
    'items': [
        {
            'name': 'macbook',
            'quantity': 1
        },
        {
            'name': 'ford fiesta',
            'quantity': 1
        },
        {
            'name': 'shoes',
            'quantity': 10
        }
    ]
}

# Example of usage
FUTURE_PAYLOAD = {
    'client_name': Join(GetField('name'), GetField('last_name'), delimiter=' '),
    'client_age': GetField('age'),
    'client_street': GetSubField(['address']['street']),
    'client_number': GetSubField(['address']['number']),
    'client_city': GetSubField(['address']['city']),
    'client_state':  GetSubField(['address']['state']),
    'client_laptop': GetFromListField(position=0),
    'client_car':  GetFromListField(condition=lambda x: x['name'] == 'car')
}

PayloadTranslator(from=BASE_PAYLOAD, to=FUTURE_PAYLOAD).translate()
# should return
{
    'client_name': 'Samuel Dantas',  # should join name and last name
    'client_age': 28,  # direct field
    'client_street':  'R. Some Fake Street',  # get it from the sub field in address
    'client_number': 123,  # get it from the sub field in address
    'client_city': 'Osasco',  # get it from the sub field in address
    'client_state': 'SP',  # get it from the sub field in address
    'client_laptop': 'macbook',  # get it from a list by position or condition
    'client_car': 'ford fiesta',  # get it from a list by position or condition
}

# possible methods
PayloadTranslator(from=BASE_PAYLOAD, to=FUTURE_PAYLOAD).errors() # return a list of errors


# possible exceptions by methods
# - translate()
#     - invalid `from` or `to` parameters
#     - invalid field to get from (it must be raised by each class of field)

