Sure, here is the Python function to find the lateral surface area of a cylinder:

```python
import math

def lateral_surface_area_cylinder(radius, height):
    """
    This function calculates the lateral surface area of a cylinder.
    The formula for the lateral surface area of a cylinder is 2*pi*radius*height.
    """
    return 2 * math.pi * radius * height

# Test the function
assert math.isclose(lateral_surface_area_cylinder(10,5), 314.1592653589793, rel_tol=0.001)
```

This function takes two parameters: the radius and the height of the cylinder. It calculates the lateral surface area using the formula `2*pi*radius*height` and returns the result. The `math.isclose` function is used to compare the result of the function with the expected result, allowing for a small relative tolerance.
