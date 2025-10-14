Here is the completed code snippet:

```
def lateralsurface_cube(side_length):
    """
    Calculate the lateral surface area of a cube given its side length.
    
    Parameters:
    side_length (float): The length of one side of the cube.
    
    Returns:
    float: The lateral surface area of the cube.
    """
    return 4 * side_length ** 2

# Test the function
assert lateralsurface_cube(5) == 100
```