Here is the completed code snippet:

```python
def tup_string(tup):
    return ''.join(tup)

assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"
```

The `tup_string` function takes a tuple as input and uses the `join` method to concatenate all the elements of the tuple into a single string. The resulting string is then returned. The `assert` statement is used to verify that the function produces the expected output.