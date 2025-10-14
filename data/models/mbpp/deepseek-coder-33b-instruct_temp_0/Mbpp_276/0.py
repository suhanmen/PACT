Here is the Python function that calculates the volume of a cylinder:

```python
import math

def volume_cylinder(radius, height):
    """
    This function calculates the volume of a cylinder.
    The volume of a cylinder is calculated as:
    V = πr²h
    where r is the radius of the base and h is the height of the cylinder.
    """
    return math.pi * radius**2 * height
```

You can test the function with the given assertion:

```python
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
```

This assertion checks if the calculated volume of a cylinder with radius 10 and height 5 is close to the expected volume (1570.7500000000002) within a relative tolerance of 0.001. If the calculated volume is not within this tolerance, the assertion will fail.
