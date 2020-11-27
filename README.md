# Payload Translator

What is that?
First I need to explain my necessity. I needed to translate a payload A for a format B, considering that the payload A has every data B needs.
Some things to consider: sometimes for satisfy a payload B field we need to join one or more fields from A, sometimes we need to sum some values from multiples fields
from A, sometimes divide or multiply. Thats the main ideia here. Get the values from a payload to fill another one that has a different structure.
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

# What it must do
- Translate from a field to another
- Raise errors for fields which doesn't match
