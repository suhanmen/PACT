Here is the Python function implemented in a markdown style code block:

```python
def empty_list(n):
    return [{} for _ in range(n)]

# Test the function
assert empty_list(5)==[{},{},{},{},{}]
```

This function uses a list comprehension to create a list of N empty dictionaries. The `_` is a conventional variable name used when the variable is not used in the loop.
