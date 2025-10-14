Here is the Python function to find the volume of a cube given its side length:

```python
def volume_cube(side_length):
    """
    This function calculates the volume of a cube given its side length.
    """
    return side_length ** 3

# Test the function
assert volume_cube(3) == 27
```

In this function, we are using the formula for the volume of a cube, which is `side_length ** 3`. The `**` operator is used for exponentiation in Python. The `assert` statement is used to test the function. If the function is working correctly, the `assert` statement will not raise an `AssertionError`.
