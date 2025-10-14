Here's the completed code snippet:

```python
import math

def angle_complex(z):
    return math.atan2(z.imag, z.real)

assert math.isclose(angle_complex(0+1j), 1.5707963267948966, rel_tol=0.001)
```

In this code, the `angle_complex` function takes a complex number `z` as input and uses the `math.atan2` function to calculate the angle of the complex number. The `math.atan2` function returns the angle in radians, which is the desired output.

The `assert` statement is used to check if the calculated angle is close to the expected value. The `math.isclose` function is used to perform the comparison with a specified relative tolerance of 0.001. If the calculated angle is within the specified tolerance of the expected value, the assertion passes.