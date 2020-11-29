# FEATURES TODO:

[X] - Get a directly field value to another:
*Ex:*
```python
# from:
{
    “test”: “test value”
}
# to:
{
    “from_test”: “test value”
}
```

[] - Get a value from a sub field (a field within a dict):
*Ex:*
```python
# from
{
    "test": "test value",
    "dict_test": {
        "first_field": "test value from first field",
        "second_field": "test value from second field"
    }
}
# to
{
    "my_first_field": "test value from first field",
    "my_second_field": "test value from second field"
}
```
