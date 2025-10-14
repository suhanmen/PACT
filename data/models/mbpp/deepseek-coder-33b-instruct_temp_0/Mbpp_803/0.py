Here is the Python function to check whether the given number is a perfect square or not:

```python
import math

def is_perfect_square(n):
    """
    Function to check whether the given number is a perfect square or not.
    """
    if n < 0:
        return False
    root = math.sqrt(n)
    return n == int(root + 0.5) ** 2

# Test the function
print(is_perfect_square(10))  # Expected output: False
```

This function works by taking the square root of the given number, rounding it to the nearest integer, and then squaring it. If the result is equal to the original number, then the number is a perfect square. If not, it is not a perfect square.
