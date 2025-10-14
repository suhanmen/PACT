Here is the Python function to convert degrees to radians:

```python
import math

def degree_to_radian(degrees):
    return degrees * (math.pi / 180)

# Test the function
assert degree_to_radian(90)==1.5707963267948966
```

This function uses the `math` module's `pi` constant and the formula for converting degrees to radians. The `assert` statement is used to test the function. If the function is implemented correctly, it should pass the test.
