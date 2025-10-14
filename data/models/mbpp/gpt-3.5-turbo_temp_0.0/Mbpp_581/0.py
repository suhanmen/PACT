Here is the completed code snippet:

```python
def surface_Area(base_edge, height):
    base_area = base_edge ** 2
    lateral_area = base_edge * height
    total_area = base_area + (2 * lateral_area)
    return total_area

assert surface_Area(3, 4) == 33
```

In this code, the `surface_Area` function takes two parameters: `base_edge` and `height`. It calculates the base area by squaring the `base_edge` value. It then calculates the lateral area by multiplying the `base_edge` with the `height`. Finally, it adds the base area and twice the lateral area to get the total surface area of the square pyramid. The function returns the total area.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `surface_Area(3, 4)` is equal to 33. If the assertion fails, an error will be raised.