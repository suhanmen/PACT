Here is the Python function to find the next perfect square greater than a given number:

```python
import math

def next_Perfect_Square(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return n
    else:
        return (int(root) + 1) ** 2

print(next_Perfect_Square(35))  # Output: 36
```

This function works by first calculating the square root of the given number. If the square of the integer part of the square root plus 0.5 is equal to the original number, then the number is a perfect square and it is returned as is. Otherwise, the next perfect square is calculated by adding 1 to the integer part of the square root and squaring the result.
