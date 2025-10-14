Here is the completed code snippet:

```python
def find_Volume(base, height, length):
    # Calculate the area of the base triangle
    base_area = 0.5 * base * height
    
    # Calculate the volume of the prism
    volume = base_area * length
    
    return volume

assert find_Volume(10, 8, 6) == 240
```

In this code, the `find_Volume` function takes three parameters: `base`, `height`, and `length`. It calculates the area of the base triangle using the formula `0.5 * base * height`. Then, it multiplies the base area by the length to find the volume of the triangular prism. Finally, it returns the volume.

The `assert` statement at the end of the code snippet checks if the function returns the expected volume of 240 for the given base, height, and length values.