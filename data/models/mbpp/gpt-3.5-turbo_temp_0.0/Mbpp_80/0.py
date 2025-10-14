Here's the completed code snippet:

```python
def tetrahedral_number(n):
    """
    Function to find the nth tetrahedral number.
    """
    return (n * (n + 1) * (n + 2)) // 6

assert tetrahedral_number(5) == 35
```

In this code, the `tetrahedral_number` function takes an integer `n` as input and calculates the nth tetrahedral number using the formula `(n * (n + 1) * (n + 2)) // 6`. The function then returns the calculated value.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `tetrahedral_number(5)` is equal to `35`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.