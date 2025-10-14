Here is the completed code snippet:

```python
def volume_cube(side_length):
    volume = side_length ** 3
    return volume

assert volume_cube(3) == 27
```

The `volume_cube` function takes in a `side_length` parameter and calculates the volume of a cube by raising the side length to the power of 3. The calculated volume is then returned.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `volume_cube(3)` returns 27. If the assertion fails, an error will be raised.