Here is the Python function implemented in a markdown style code block:

```python
def check_none(tup):
    """
    Write a function to check if the given tuple has any none value or not.
    """
    return None in tup

# Test the function
print(check_none((10, 4, 5, 6, None)))  # Expected output: True
```

In this function, we use the `in` operator to check if `None` is in the tuple. If `None` is found, the function returns `True`, otherwise it returns `False`.
