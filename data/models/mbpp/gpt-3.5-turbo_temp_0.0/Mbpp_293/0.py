Here is the completed code snippet:

```python
import math

def otherside_rightangle(side1, side2):
    side3 = math.sqrt(side1**2 + side2**2)
    return side3

assert otherside_rightangle(7, 8) == 10.63014581273465
```

In this code, we import the `math` module to use the `sqrt` function. The `otherside_rightangle` function takes two arguments, `side1` and `side2`, representing the lengths of the two sides of the right-angled triangle. It calculates the length of the third side using the Pythagorean theorem and returns the result. The `assert` statement checks if the calculated value matches the expected value and raises an error if they are not equal.