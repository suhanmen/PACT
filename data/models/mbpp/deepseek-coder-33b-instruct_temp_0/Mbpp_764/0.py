Here is the Python function implemented in a markdown style code block:

```python
def number_ctr(s):
    return sum(c.isdigit() for c in s)

# Test the function
assert number_ctr('program2bedone') == 1
```

This function works by iterating over each character in the string `s` and checking if it is a digit using the `isdigit()` method. If the character is a digit, `isdigit()` returns `True`, otherwise it returns `False`. The `sum()` function then adds up all the `True` values, which gives the total number of digits in the string.
