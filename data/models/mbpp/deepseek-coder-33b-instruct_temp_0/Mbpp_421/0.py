Here is the Python function implemented in a markdown style code block:

```python
def concatenate_tuple(tup, delimiter='-'):
    return delimiter.join(str(i) for i in tup)

print(concatenate_tuple(("ID", "is", 4, "UTS")))
```

This function takes a tuple and a delimiter as input. It uses the `join` method of the string class to concatenate each element of the tuple. The `str(i)` is used to convert each element of the tuple to a string, as the `join` method only works with strings. The default delimiter is '-', but it can be changed by passing a second argument to the function.
