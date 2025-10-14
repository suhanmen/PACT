Here is the Python function to get the angle of a complex number:

```python
import math

def angle_complex(z):
    """
    This function returns the angle of a complex number.
    """
    return math.atan2(z.imag, z.real)
```

You can use the `math.atan2` function to calculate the angle of a complex number. This function takes two arguments: the imaginary part of the complex number and the real part of the complex number. It returns the angle in radians.

You can use the `math.isclose` function to compare the result of `angle_complex(0,1j)` with `1.5707963267948966`. The `rel_tol` parameter is used to specify the relative tolerance – the maximum allowed difference between `angle_complex(0,1j)` and `1.5707963267948966` as a fraction of the magnitude of the second value.
