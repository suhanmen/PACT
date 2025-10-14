Here is the completed code snippet:

```python
def ascii_value(char):
    return ord(char)

assert ascii_value('A') == 65
```

The `ord()` function in Python returns the ASCII value of a character. In the `ascii_value()` function, we simply call `ord(char)` to get the ASCII value of the input character. The `assert` statement is used to verify that the function returns the expected result.