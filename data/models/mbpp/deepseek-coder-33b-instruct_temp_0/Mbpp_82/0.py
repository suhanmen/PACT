Here is the Python function to find the volume of a sphere:

```python
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Test the function
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
```

This function uses the formula for the volume of a sphere: `(4/3) * π * r^3`, where `r` is the radius of the sphere. The `math.isclose` function is used to compare the result of the function with the expected result, allowing for a small relative tolerance.
