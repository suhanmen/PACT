Here is the completed code snippet:

```python
import cmath

def polar_rect(r, theta):
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return (x, y)

assert polar_rect(3, 4) == ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
```

In this code, we use the `cmath` module to handle complex numbers. The `polar_rect` function takes two parameters: `r` for the radius and `theta` for the angle in radians. It calculates the rectangular coordinates `(x, y)` using the formulas `x = r * cos(theta)` and `y = r * sin(theta)`. Finally, we assert that the result of `polar_rect(3, 4)` matches the expected output.