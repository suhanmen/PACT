Here is the completed code snippet:

```python
def remove_lowercase(string):
    new_string = ''
    for char in string:
        if not char.islower():
            new_string += char
    return new_string

assert remove_lowercase("PYTHon") == 'PYTH'
```