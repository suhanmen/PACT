Here is the completed code snippet:

```python
def replace_blank(string, character):
    return string.replace(" ", character)

assert replace_blank("hello people", '@') == "hello@people"
```

In this code, the `replace_blank` function takes in two parameters: `string` and `character`. It uses the `replace` method of strings to replace all occurrences of a blank space with the specified character. The modified string is then returned.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if `replace_blank("hello people", '@')` is equal to `"hello@people"`. If the condition is true, the code continues execution. If the condition is false, an `AssertionError` is raised.