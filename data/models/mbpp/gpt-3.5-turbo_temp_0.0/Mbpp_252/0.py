Here is the completed code snippet:

```python
import cmath

def convert(complex_num):
    polar_coords = cmath.polar(complex_num)
    return polar_coords

assert convert(1) == (1.0, 0.0)
```

In this code, we import the `cmath` module which provides mathematical functions for complex numbers. The `polar()` function from `cmath` is used to convert the complex number to polar coordinates. The function `convert()` takes a complex number as input and returns its polar coordinates. The `assert` statement is used to verify that the function returns the expected result.