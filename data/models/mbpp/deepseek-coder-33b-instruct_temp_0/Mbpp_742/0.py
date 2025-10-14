Here is the Python function to calculate the area of a tetrahedron:

```python
import math

def area_tetrahedron(side):
    """
    Calculate the area of a tetrahedron.
    """
    return math.sqrt(3) * side ** 2

# Test the function
assert math.isclose(area_tetrahedron(3), 15.588457268119894, rel_tol=1e-9)
```

This function uses the formula for the area of a tetrahedron, which is `sqrt(3) * side^2`. The `math.isclose` function is used to compare the result of the function with the expected result, allowing for a small margin of error due to floating point precision.
