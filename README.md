# Payload Translator
:hacktoberfest

What is that?
First I need to explain my necessity. I needed to translate a payload A for a format B, considering that the payload A has every data B needs.
Some things to consider: sometimes for satisfy a payload B field we need to join one or more fields from A, sometimes we need to sum some values from multiples fields
from A, sometimes divide or multiply. Thats the main ideia here. Get the values from a payload to fill another one that is in a different structure.
Example:

*ORIGINAL PAYLOAD*
```python
{
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
```

*SHOULD BE TRANSLATED TO*
```python
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
```

# Usage Examples
```python
ORIGINAL_PAYLOAD = {
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

PAYLOAD_MAPPING = {
    'client_name': Join(GetFrom('name'), GetFrom('last_name'), delimiter=' '),
    'client_age': GetFrom('age'),
    'client_street': GetFrom(('address', 'street')),
    'client_number': GetFrom(('address', 'number')),
    'client_city': GetFrom(('address', 'city')),
    'client_state':  GetFrom(('address', 'state')),
    'client_laptop': GetFromListField(position=0),
    'client_car':  GetFromListField(condition=lambda x: x['name'] == 'car')
}

PayloadTranslator(_from=ORIGINAL_PAYLOAD, _to=PAYLOAD_MAPPING).translate()
# {
#     'client_name': 'Samuel Dantas',
#     'client_age': 28,
#     'client_street':  'R. Some Fake Street',
#     'client_number': 123,
#     'client_city': 'Osasco',
#     'client_state': 'SP',
#     'client_laptop': 'macbook',
#     'client_car': 'ford fiesta',
# }
```

# Next features
- Mathematical operators: sum, sub, divide, multiply
- Custom operator. The same behaviour of GetFrom but parsing with a custom function
- Validators by type and custom functions
