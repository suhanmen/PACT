Here is the Python function to convert RGB color to HSV color:

```python
def rgb_to_hsv(r, g, b):
    # Normalize the RGB values
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Find the maximum and minimum values of R, G, B
    cmax = max(r, g, b)   
    cmin = min(r, g, b)   
    diff = cmax-cmin  

    # Calculate hue
    if cmax == cmin:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    else:
        h = (60 * ((r - g) / diff) + 240) % 360

    # Calculate saturation
    if cmax == 0:
        s = 0
    else:
        s = (diff/cmax)*100

    # Calculate value
    v = cmax*100

    return round(h, 2), round(s, 2), round(v, 2)

# Test the function
print(rgb_to_hsv(255, 255, 255))  # Output: (0.0, 0.0, 100.0)
```

This function first normalizes the RGB values to be between 0 and 1. Then it calculates the hue, saturation, and value based on the formulae provided in the GeeksforGeeks link. The hue is calculated differently based on which of the RGB values is the maximum. The saturation is the ratio of the difference between the maximum and minimum RGB values to the maximum, multiplied by 100 to get a percentage. The value is simply the maximum RGB value multiplied by 100. The function returns the hue, saturation, and value as a tuple, rounded to two decimal places.
