Here is the Python function implemented in a markdown style code block:

```python
def tuple_modulo(t1, t2):
    return tuple(a % b for a, b in zip(t1, t2))
```

This function uses the `zip` function to pair up the elements of the two tuples, then uses a generator expression to perform the modulo operation on each pair. The results are collected into a new tuple which is returned.
