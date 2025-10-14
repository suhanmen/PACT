Here is the completed code snippet:

```python
import math

def lateralsurface_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    return lateral_surface_area

assert lateralsurface_cone(5, 12) == 204.20352248333654
```

In this code, we first import the `math` module to access the mathematical functions. Then, we define a function called `lateralsurface_cone` that takes two parameters: `r` for the radius and `h` for the height of the cone.

Inside the function, we calculate the slant height of the cone using the Pythagorean theorem: `slant_height = math.sqrt(r**2 + h**2)`. Then, we calculate the lateral surface area using the formula: `lateral_surface_area = math.pi * r * slant_height`.

Finally, we return the calculated lateral surface area and use an `assert` statement to check if the function returns the expected value for the given example.