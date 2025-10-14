Here is the Python function to find the nth nonagonal number:

```python
def is_nonagonal(n):
    return n * (7 * n - 5) // 2

# Test the function
assert is_nonagonal(10) == 325
```

This function works by using the formula for the nth nonagonal number, which is `n * (7 * n - 5) // 2`. The `//` operator is used for integer division, which discards the fractional part and returns only the integer part.
