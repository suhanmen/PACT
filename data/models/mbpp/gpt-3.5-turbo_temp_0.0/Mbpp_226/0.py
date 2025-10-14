Here is the completed code snippet:

```python
def odd_values_string(string):
    return string[::2]

assert odd_values_string('abcdef') == 'ace'
```

In this code, the `odd_values_string` function takes a string as input. It uses slicing with a step of 2 (`[::2]`) to extract the characters at odd index positions. The function then returns the resulting string. The `assert` statement is used to verify that the function returns the expected output.