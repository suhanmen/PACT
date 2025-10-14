Here's the completed code snippet:

```python
def is_octagonal(n):
    return n * (3 * n - 2)

assert is_octagonal(5) == 65
```

The function `is_octagonal` takes an integer `n` as input and returns the nth octagonal number. The formula to calculate the nth octagonal number is `n * (3 * n - 2)`. The `assert` statement is used to verify that `is_octagonal(5)` returns the expected result of `65`.