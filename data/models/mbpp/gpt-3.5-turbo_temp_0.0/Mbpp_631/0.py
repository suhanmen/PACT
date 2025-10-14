Here is the completed code snippet:

```python
def replace_spaces(string):
    return string.replace(' ', '_').replace('_', ' ')

assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
```

The `replace_spaces` function takes a string as input and uses the `replace` method to replace all occurrences of a whitespace character with an underscore, and vice versa. The first `replace` call replaces all spaces with underscores, and the second `replace` call replaces all underscores with spaces. The modified string is then returned. The `assert` statement checks if the function returns the expected result for the given input.