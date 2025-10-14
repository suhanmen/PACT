Here is the completed code snippet:

```python
import math

def area_tetrahedron(side_length):
    """
    Calculate the area of a tetrahedron given the length of its side.
    """
    area = math.sqrt(3) * side_length**2
    return area

assert area_tetrahedron(3) == 15.588457268119894
```

In this code, we import the `math` module to access the square root function. The `area_tetrahedron` function takes the length of a side as input and calculates the area of the tetrahedron using the formula `area = sqrt(3) * side_length^2`. Finally, we use an `assert` statement to verify that the calculated area matches the expected result.