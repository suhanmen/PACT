Sure, here is the Python function to find the surface area of a cylinder:

```python
import math

def surfacearea_cylinder(radius, height):
    """
    Function to find the surface area of a cylinder.
    """
    # Surface area of a cylinder = 2*pi*radius*(radius+height)
    surface_area = 2 * math.pi * radius * (radius + height)
    return round(surface_area, 2)

# Test the function
assert surfacearea_cylinder(10,5)==942.45
```

This function uses the formula for the surface area of a cylinder, which is `2*pi*radius*(radius+height)`. The `math.pi` constant is used to get the value of pi, and the `round` function is used to round the result to two decimal places.
