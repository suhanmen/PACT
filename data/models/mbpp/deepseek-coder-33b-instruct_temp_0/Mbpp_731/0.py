Here is the Python function to find the lateral surface area of a cone:

```python
import math

def lateralsurface_cone(r, h):
    return math.pi * r * math.sqrt(r**2 + h**2)

# Test the function
print(lateralsurface_cone(5,12))
```

This function uses the formula for the lateral surface area of a cone: `π * r * sqrt(r^2 + h^2)`. The `math.sqrt` function is used to calculate the square root, and `math.pi` is used to get the value of π.

Please note that the `assert` statement in the problem statement is not a part of the function. It is used to test the function. The `assert` statement checks if the result of the function is equal to the expected result. If the result is not equal, the `assert` statement will raise an `AssertionError`.
