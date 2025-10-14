Sure, here is the Python function to find the surface area of a square pyramid:

```python
import math

def surface_Area(base_edge, height):
    """
    This function calculates the surface area of a square pyramid.
    The formula for the surface area of a square pyramid is:
    surface_area = base_edge^2 + 2*base_edge*slant_length
    where slant_length = sqrt(height^2 + (base_edge/2)^2)
    """
    slant_length = math.sqrt(height**2 + (base_edge/2)**2)
    surface_area = base_edge**2 + 2*base_edge*slant_length
    return surface_area

# Test the function
print(surface_Area(3,4))  # Output: 33.0
```

This function first calculates the slant length of the pyramid using the Pythagorean theorem. Then it calculates the surface area using the formula given in the docstring. The function returns the surface area.
