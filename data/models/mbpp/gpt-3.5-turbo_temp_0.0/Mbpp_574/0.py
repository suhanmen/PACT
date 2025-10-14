Here is the completed code snippet:

```python
import math

def surfacearea_cylinder(radius, height):
    # Calculate the surface area of the cylinder
    base_area = math.pi * radius**2
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * base_area + lateral_area

    return round(total_area, 2)

assert surfacearea_cylinder(10, 5) == 942.45
```

In this code, we import the `math` module to access the value of pi. The `surfacearea_cylinder` function takes two parameters: `radius` and `height`. It calculates the base area, lateral area, and total area of the cylinder using the given formulas. Finally, the `total_area` is rounded to two decimal places and returned. The `assert` statement checks if the calculated surface area matches the expected value and raises an error if they are not equal.