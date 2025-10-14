Here is the Python function to remove uneven elements in the nested mixed tuple:

```python
def extract_even(t):
    if isinstance(t, tuple):
        return tuple(extract_even(i) for i in t if (isinstance(i, int) and i % 2 == 0) or isinstance(i, tuple))
    else:
        return ()

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))
```

This function works by checking if the input is a tuple. If it is, it creates a new tuple that includes the result of recursively calling `extract_even` on each element of the input tuple, but only if the element is an integer and is even, or if the element is a tuple itself. If the input is not a tuple, it returns an empty tuple.

The `isinstance(i, int) and i % 2 == 0` condition checks if the element is an integer and is even. The `isinstance(i, tuple)` condition checks if the element is a tuple. If either of these conditions is true, the element is included in the new tuple. If neither condition is true, the element is not included.
