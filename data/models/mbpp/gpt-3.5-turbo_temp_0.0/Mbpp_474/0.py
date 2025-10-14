Here is the completed code snippet:

```python
def replace_char(string, old_char, new_char):
    return string.replace(old_char, new_char)

assert replace_char("polygon", 'y', 'l') == "pollgon"
```

The `replace_char` function takes three parameters: `string`, `old_char`, and `new_char`. It uses the `replace` method of the string to replace all occurrences of `old_char` with `new_char`. The modified string is then returned.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if `replace_char("polygon", 'y', 'l')` is equal to `"pollgon"`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.