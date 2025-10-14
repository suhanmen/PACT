Here is the completed code snippet:

```python
def replace_spaces(string):
    return string.replace(" ", "%20")

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
```

The `replace_spaces` function takes a string as input and uses the `replace` method to replace all occurrences of a space with '%20'. The modified string is then returned. The `assert` statement is used to verify that the function produces the expected output.