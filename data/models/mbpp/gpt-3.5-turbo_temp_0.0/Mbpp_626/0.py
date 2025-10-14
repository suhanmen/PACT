Here is the completed code snippet:

```python
import math

def triangle_area(radius):
    if radius <= 0:
        return None
    
    # Calculate the diameter of the semicircle
    diameter = 2 * radius
    
    # Calculate the base of the triangle
    base = diameter
    
    # Calculate the height of the triangle
    height = radius
    
    # Calculate the area of the triangle
    area = 0.5 * base * height
    
    return area

assert triangle_area(-1) == None
```

In this code, we first check if the given radius is less than or equal to 0. If it is, we return None as the area cannot be calculated. Otherwise, we calculate the diameter of the semicircle by multiplying the radius by 2. The base of the triangle is equal to the diameter, and the height is equal to the radius. Finally, we calculate the area of the triangle using the formula 0.5 * base * height and return the result.