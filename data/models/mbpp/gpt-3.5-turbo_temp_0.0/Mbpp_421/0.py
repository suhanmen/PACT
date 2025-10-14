Here is the completed code snippet:

```python
def concatenate_tuple(tup, delimiter="-"):
    return delimiter.join(str(element) for element in tup)

assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'
```

In this code, the `concatenate_tuple` function takes a tuple `tup` and a delimiter (defaulting to "-") as parameters. It uses a generator expression to convert each element of the tuple to a string, and then joins them together using the delimiter. The resulting string is returned.

The `assert` statement is used to verify that the function produces the expected output.