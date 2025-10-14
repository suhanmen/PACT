Here is the Python function to find the quotient of two numbers (rounded down to the nearest integer):

```python
def find(num1, num2):
    return num1 // num2

# Test the function
assert find(10,3) == 3
```

In this function, the `//` operator is used for integer division, which rounds down to the nearest integer. The `assert` statement is used to test the function. If the result of the `find` function is not equal to `3` when called with `10` and `3`, the `assert` statement will raise an `AssertionError`.
