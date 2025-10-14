Here is the Python function to find the first digit of a given number:

```python
def first_Digit(num):
    """
    This function takes an integer as input and returns the first digit of the number.
    """
    while num >= 10:
        num = num // 10
    return num

# Test the function
assert first_Digit(123) == 1
```

This function works by continuously dividing the number by 10 until it is less than 10. The remainder of the division is the first digit of the number.
