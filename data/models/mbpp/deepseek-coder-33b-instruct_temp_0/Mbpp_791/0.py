Here is the Python function to remove tuples from the given tuple:

```python
def remove_nested(t):
    return tuple(i for i in t if not isinstance(i, tuple))

# Test the function
print(remove_nested((1, 5, 7, (4, 6), 10)))  # Output: (1, 5, 7, 10)
```

In this function, we use a generator expression to iterate over each item in the input tuple. The `isinstance(i, tuple)` function checks if the current item is a tuple. If it is, the item is not included in the output tuple. If it is not a tuple, the item is included in the output tuple.
