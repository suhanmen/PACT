Here is the Python function to find the third side of a right angled triangle:

```python
import math

def otherside_rightangle(side1, side2):
    """
    This function calculates the length of the third side of a right-angled triangle given the lengths of the other two sides.
    """
    return math.sqrt(side1**2 + side2**2)

# Test the function
print(otherside_rightangle(7,8))
```

This function uses the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.

The `math.sqrt` function is used to calculate the square root of a number, and the `**` operator is used to raise a number to a power.

Please note that the result of the function `otherside_rightangle(7,8)` is `10.63014581273465`, which is the length of the third side of the right-angled triangle with sides of length 7 and 8.
