Here is the Python function to find the ratio of zeroes to non-zeroes in an array of integers:

```python
import math

def zero_count(arr):
    zeroes = arr.count(0)
    non_zeroes = len(arr) - zeroes
    return zeroes / non_zeroes

# Test the function
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
```

This function works by first counting the number of zeroes in the array using the `count` method, then subtracting this from the total length of the array to get the number of non-zero elements. It then returns the ratio of zeroes to non-zeroes.

The `math.isclose` function is used to compare the result of the `zero_count` function with the expected result, allowing for a small margin of error due to floating point precision.
