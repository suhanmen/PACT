Here is the Python function to find the volume of a triangular prism:

```python
def find_Volume(base, height, length):
    """
    This function calculates the volume of a triangular prism.
    The volume of a triangular prism is calculated by multiplying the area of the base by the height.
    The area of the base of a triangle is calculated by multiplying 1/2 (base * height).
    """
    return 0.5 * base * height * length
```

You can test the function with the following code:

```python
assert find_Volume(10,8,6) == 240
```

This code will raise an `AssertionError` if the function does not return the expected result.
