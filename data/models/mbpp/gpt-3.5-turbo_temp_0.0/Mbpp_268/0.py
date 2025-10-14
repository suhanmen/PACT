Here is the completed code snippet:

```python
def find_star_num(n):
    """
    Function to find the n'th star number.
    """
    star_num = 6 * n * (n - 1) + 1
    return star_num

assert find_star_num(3) == 37
```

In this code, the `find_star_num` function takes an integer `n` as input and calculates the n'th star number using the formula `6 * n * (n - 1) + 1`. The calculated star number is then returned as the output.

The `assert` statement is used to verify that the function returns the expected result for the given input. In this case, it checks if `find_star_num(3)` is equal to `37`. If the condition is true, the code continues execution. If the condition is false, an `AssertionError` is raised.