Here is the completed code snippet:

```python
def remove_nested(t):
    result = []
    for item in t:
        if isinstance(item, tuple):
            result.extend(item)
        else:
            result.append(item)
    return tuple(result)

assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
```

The `remove_nested` function takes a tuple `t` as input and returns a new tuple with all the nested tuples removed. It iterates over each item in the input tuple and checks if it is a tuple using the `isinstance` function. If it is a tuple, it extends the `result` list with its elements. If it is not a tuple, it appends it directly to the `result` list. Finally, it returns the `result` list converted back to a tuple.

The `assert` statement at the end checks if the function produces the expected output for the given example.