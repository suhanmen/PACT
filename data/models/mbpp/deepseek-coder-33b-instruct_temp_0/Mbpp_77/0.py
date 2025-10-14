Here is the Python function to find whether a number is divisible by 11:

```python
def is_divisible_by_11(n):
    """
    This function checks if a number is divisible by 11.
    """
    return n % 11 == 0

# Test the function
print(is_divisible_by_11(12345))  # Output: False
```

In this function, we use the modulus operator (%) to find the remainder of the division of the number by 11. If the remainder is 0, the number is divisible by 11, so the function returns True. Otherwise, it returns False.
