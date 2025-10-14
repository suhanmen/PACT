Here's the completed code snippet:

```python
"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""

def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value - min_value

    if max_value == min_value:
        h = 0
    elif max_value == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_value == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif max_value == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    if max_value == 0:
        s = 0
    else:
        s = (diff / max_value) * 100

    v = max_value * 100

    return round(h, 2), round(s, 2), round(v, 2)

assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
```

This code defines a function `rgb_to_hsv` that takes three arguments `r`, `g`, and `b` representing the red, green, and blue values of an RGB color, respectively. The function converts the RGB color to HSV color using the formulas provided in the link you mentioned. The resulting HSV color is returned as a tuple `(h, s, v)`, where `h` represents the hue, `s` represents the saturation, and `v` represents the value. The function also includes an assertion to verify that the conversion is correct for the given RGB color (255, 255, 255).