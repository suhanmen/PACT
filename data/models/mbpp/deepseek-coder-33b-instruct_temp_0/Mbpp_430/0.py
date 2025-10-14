Here is the Python function to find the directrix of a parabola:

```python
def parabola_directrix(a, b, c):
    """
    This function calculates the directrix of a parabola given the coefficients a, b, and c.
    The directrix is calculated as -b/2a.
    """
    return -b / (2 * a)

# Test the function
assert parabola_directrix(5,3,2)==-198
```

Please note that the function `parabola_directrix` takes three arguments: `a`, `b`, and `c`, which are the coefficients of the quadratic equation `ax^2 + bx + c = 0`. The function returns the directrix of the parabola, which is calculated as `-b/2a`.

The assertion `assert parabola_directrix(5,3,2)==-198` is used to test the function. If the function is implemented correctly, this assertion should not raise an `AssertionError`.
