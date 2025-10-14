Here is the completed code snippet:

```python
import math

def parabola_directrix(a, b, c):
    # Calculate the directrix using the formula: x = -c/(4a)
    directrix = -c / (4 * a)
    return directrix

assert parabola_directrix(5, 3, 2) == -198
```

In this code, the function `parabola_directrix` takes three parameters `a`, `b`, and `c`, which represent the coefficients of the quadratic equation in the form `ax^2 + bx + c`. The function calculates the directrix of the parabola using the formula `x = -c/(4a)`. The calculated directrix is then returned by the function.

The `assert` statement at the end of the code snippet checks if the calculated directrix is equal to the expected value `-198`. If the assertion fails, an `AssertionError` will be raised.