Here is the Python function to find the surface area of a cube of a given size:

```python
def surfacearea_cube(size):
    """
    This function calculates the surface area of a cube of a given size.
    """
    return 6 * size * size

# Test the function
assert surfacearea_cube(5)==150
```

In this function, the surface area of a cube is calculated as 6 times the square of the size of the cube. The `assert` statement is used to test the function. If the result of the function is not equal to 150, the `assert` statement will raise an `AssertionError`.
