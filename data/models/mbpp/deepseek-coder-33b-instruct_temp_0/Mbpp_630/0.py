Here is the Python function to solve the problem:

```python
def get_coordinates(coordinate):
    x, y = coordinate
    return [[x-1, y-1], [x-1, y], [x-1, y+1], 
            [x, y-1], [x, y], [x, y+1], 
            [x+1, y-1], [x+1, y], [x+1, y+1]]

print(get_coordinates((3, 4)))
```

This function takes a tuple of two integers as input, representing a coordinate in a 2D grid. It then generates all the adjacent coordinates of the given coordinate, and returns them as a list of lists.

The function works by first unpacking the input tuple into two variables, `x` and `y`. It then generates all the possible combinations of `x` and `y` that are one unit away from the original coordinate, and returns them as a list of lists.

The `print` statement at the end is used to test the function with the given example. If the function is implemented correctly, it should print the expected output.
