Here is the Python function implemented in a markdown style code block:

```python
def check_K(tup, k):
    """
    Write a function to check if the given tuples contain the k or not.
    """
    return k in tup

# Test the function
assert check_K((10, 4, 5, 6, 8), 6) == True
```

In this function, we use the `in` operator to check if `k` is in the tuple `tup`. If `k` is in `tup`, the function returns `True`, otherwise it returns `False`.
