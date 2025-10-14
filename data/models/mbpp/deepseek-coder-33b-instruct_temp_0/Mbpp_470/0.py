Here is the Python function implemented in a markdown style code block:

```python
def add_pairwise(tup):
    return tuple(tup[i] + tup[i + 1] for i in range(len(tup) - 1))
```

This function takes a tuple as an argument and returns a new tuple where each element is the sum of the corresponding pair of elements in the original tuple. The `range(len(tup) - 1)` generates indices for the tuple, and `tup[i] + tup[i + 1]` adds the pairwise elements. The `tuple()` function is used to convert the generator expression into a tuple.
