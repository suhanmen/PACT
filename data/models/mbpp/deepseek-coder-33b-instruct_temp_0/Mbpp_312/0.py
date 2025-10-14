Here is the Python function to find the volume of a cone:

```python
import math

def volume_cone(radius, height):
    """
    This function calculates the volume of a cone.
    The volume of a cone is given by the formula:
    V = (1/3) * π * r^2 * h
    where r is the radius of the base and h is the height of the cone.
    """
    return (1/3) * math.pi * radius**2 * height
```

You can use the `math.isclose` function to check if the calculated volume is close to the expected volume. Here is how you can do it:

```python
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
```

This will raise an `AssertionError` if the calculated volume is not close to the expected volume. The `rel_tol` parameter is the relative tolerance – it represents the maximum allowed difference between `volume_cone(5,12)` and `314.15926535897927`, relative to the magnitude of the later.
