Here's the completed code snippet:

```python
def is_nonagonal(n):
    return n * (7 * n - 5) // 2

assert is_nonagonal(10) == 325
```

The function `is_nonagonal` takes an integer `n` as input and returns the nth nonagonal number. The formula to calculate the nth nonagonal number is `n * (7 * n - 5) // 2`. The `//` operator is used for integer division to ensure the result is an integer.

The `assert` statement is used to verify that the function returns the correct result for the given input. In this case, it checks if `is_nonagonal(10)` is equal to `325`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.