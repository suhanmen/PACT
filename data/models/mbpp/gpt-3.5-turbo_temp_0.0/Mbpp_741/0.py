Here is the completed code snippet:

```python
def all_Characters_Same(string):
    return all(char == string[0] for char in string)

assert all_Characters_Same("python") == False
```

The `all_Characters_Same` function takes a string as input and checks if all the characters in the string are the same. It does this by comparing each character in the string to the first character using a generator expression and the `all` function. If all the characters are the same, the function returns `True`, otherwise it returns `False`. The `assert` statement is used to verify that the function behaves as expected.