Here's the completed code snippet:

```python
def remove_whitespaces(string):
    return string.replace(" ", "")

assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
```

The `remove_whitespaces` function takes a string as input and uses the `replace` method to remove all occurrences of whitespace characters (spaces) from the string. The resulting string is then returned.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if `remove_whitespaces(' Google    Flutter ')` is equal to `'GoogleFlutter'`. If the condition is true, the program continues execution without any output. If the condition is false, an `AssertionError` is raised.