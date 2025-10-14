Here is the Python function implemented in a markdown style code block:

```python
import math

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        return 0.5 * radius ** 2 * math.radians(angle)

# Test the function
print(sector_area(4, 45))
```

This function first checks if the angle is larger than 360 degrees. If it is, the function returns None. Otherwise, it calculates the area of the sector using the formula for the area of a sector, which is 1/2 * r^2 * θ, where r is the radius of the circle and θ is the central angle of the sector. The central angle is converted to radians using the `math.radians()` function before it is used in the calculation.
