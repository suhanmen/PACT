Here is the Python function implemented in a markdown style code block:

```python
import math

def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)

assert math.isclose(multiply_num([8, 2, 3, -1, 7]), -67.2, rel_tol=0.001)
```

This function takes a list of numbers as input, multiplies all the numbers in the list, and then divides the result by the length of the list. The `math.isclose()` function is used to compare the result of the function with the expected result, allowing for a small margin of error due to floating point precision.
