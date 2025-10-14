Here is the Python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.

```python
import math

def triangle_area(radius):
    if radius < 0:
        return None
    else:
        # The area of a triangle is given by the formula 1/2 * base * height
        # In this case, the base is the diameter of the semicircle (2*radius)
        # and the height is the radius of the semicircle
        area = 0.5 * 2 * radius * radius
        return area
```

This function first checks if the radius is less than 0. If it is, it returns None as per the problem statement. If the radius is not less than 0, it calculates the area of the largest triangle that can be inscribed in the semicircle using the formula for the area of a triangle (1/2 * base * height). The base of the triangle is the diameter of the semicircle (2*radius), and the height is the radius of the semicircle.
