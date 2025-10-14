Here is the Python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

```python
def is_Sum_Of_Powers_Of_Two(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            return False
    return True
```

This function works by continuously dividing the input number by 2 until it reaches 1. If at any point the number is not divisible by 2, it returns False, indicating that the number cannot be represented as a sum of non-zero powers of 2. If the number is divisible by 2, it continues to the next iteration. If the number is 1, it returns True, indicating that the number can be represented as a sum of non-zero powers of 2.
