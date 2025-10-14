Here is the Python function to find nth centered hexagonal number:

```python
def centered_hexagonal_number(n):
    return n * (2 * n - 1)

# Test the function
assert centered_hexagonal_number(10) == 271
```

This function works by using the formula for the nth centered hexagonal number, which is n * (2n - 1). The function takes an integer n as input and returns the nth centered hexagonal number. The test case asserts that the 10th centered hexagonal number is 271.
