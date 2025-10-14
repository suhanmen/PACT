Here is the completed code snippet:

```python
def hexagonal_num(n):
    """
    Function to find the nth hexagonal number.
    """
    return n * (2 * n - 1)

assert hexagonal_num(10) == 190
```

The `hexagonal_num` function takes an integer `n` as input and returns the nth hexagonal number. The formula to calculate the nth hexagonal number is `n * (2 * n - 1)`. The `assert` statement is used to verify that the function returns the correct value for the given input.