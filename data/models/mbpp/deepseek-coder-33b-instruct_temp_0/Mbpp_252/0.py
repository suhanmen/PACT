Here is the Python function to convert complex numbers to polar coordinates:

```python
import cmath

def convert(complex_num):
    """
    Convert complex numbers to polar coordinates.
    """
    return cmath.polar(complex_num)

# Test the function
assert convert(1) == (1.0, 0.0)
```

In this function, we use the `cmath.polar()` function, which converts a complex number to polar coordinates. The function returns a tuple of the form (magnitude, phase). The magnitude is the distance from the origin to the point in the complex plane, and the phase is the angle between the positive real axis and the vector from the origin to the point.
