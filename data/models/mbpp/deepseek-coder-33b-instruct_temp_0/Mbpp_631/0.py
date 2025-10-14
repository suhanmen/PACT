Here is the Python function implemented in a markdown style code block:

```python
def replace_spaces(s):
    """
    Replace whitespaces with an underscore and vice versa in a given string.
    """
    result = ''
    for char in s:
        if char == ' ':
            result += '_'
        elif char == '_':
            result += ' '
        else:
            result += char
    return result
```

You can test the function with the following code:

```python
print(replace_spaces('Jumanji The Jungle'))  # Output: Jumanji_The_Jungle
```
