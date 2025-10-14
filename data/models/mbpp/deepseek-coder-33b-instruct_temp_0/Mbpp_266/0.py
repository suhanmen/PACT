Here is the Python function to find the lateral surface area of a cube:

```python
def lateralsurface_cube(side_length):
    """
    Function to find the lateral surface area of a cube given its side length.
    """
    return 4 * side_length * side_length

# Test the function
assert lateralsurface_cube(5) == 100
```

In this function, the lateral surface area of a cube is calculated as 4 times the square of its side length. The function is then tested with an assertion to ensure it is working correctly.
