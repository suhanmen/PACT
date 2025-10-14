Here's the completed code snippet:

```python
def is_num_decagonal(n):
    return n * (7 * n - 5)

assert is_num_decagonal(3) == 27
```

The function `is_num_decagonal` takes an integer `n` as input and returns the nth decagonal number. The formula to calculate the nth decagonal number is `n * (7 * n - 5)`. The `assert` statement is used to verify that `is_num_decagonal(3)` returns the expected result of 27.