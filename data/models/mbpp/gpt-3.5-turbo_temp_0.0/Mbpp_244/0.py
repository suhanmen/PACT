Here is the completed code snippet:

```python
import math

def next_Perfect_Square(num):
    # Find the square root of the given number
    sqrt = math.isqrt(num)
    
    # Increment the square root by 1 to get the next perfect square
    next_square = (sqrt + 1) ** 2
    
    return next_square

assert next_Perfect_Square(35) == 36
```

In this code, we use the `math.isqrt()` function from the `math` module to find the square root of the given number. Then, we increment the square root by 1 and square it to get the next perfect square. Finally, we return the next perfect square. The `assert` statement is used to verify that the function returns the expected result.