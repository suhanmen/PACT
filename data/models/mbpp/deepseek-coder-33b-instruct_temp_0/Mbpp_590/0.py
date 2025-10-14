Here is the Python function to convert polar coordinates to rectangular coordinates:

```python
import cmath

def polar_rect(r, theta):
    real = r * cmath.cos(theta)
    imag = r * cmath.sin(theta)
    return (real, imag)
```

This function uses the `cmath` module to handle complex numbers. The `cmath.cos` and `cmath.sin` functions are used to calculate the cosine and sine of the angle, respectively. The result is then multiplied by the radius to get the rectangular coordinates.

Please note that the `cmath` module is used to handle complex numbers, which are numbers with a real part and an imaginary part. The `cmath` module provides functions for complex number arithmetic.

The `assert` statement in the problem statement is not valid Python code. It is used to test the function and check if it returns the expected result. In Python, you can use the `assert` statement to test if a condition is true. If the condition is not true, an `AssertionError` is raised.
