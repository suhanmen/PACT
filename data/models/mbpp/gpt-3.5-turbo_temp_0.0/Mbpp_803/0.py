Here is the completed code snippet:

```python
import math

def is_perfect_square(num):
    sqrt = math.isqrt(num)
    return sqrt * sqrt == num

assert not is_perfect_square(10)
```

In this code, we import the `math` module to use the `isqrt()` function, which returns the integer square root of a number. We then calculate the square root of the given number using `isqrt()` and check if the square of the square root is equal to the original number. If it is, then the number is a perfect square and the function returns `True`. Otherwise, it returns `False`.

The `assert` statement is used to verify that the function returns the expected result for the given test case. In this case, we expect the number 10 to not be a perfect square, so the assertion should pass.