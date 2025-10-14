Here is the Python function to find the last digit of a given number:

```python
def last_Digit(n):
    return n % 10

# Test the function
assert last_Digit(123) == 3
```

This function works by using the modulus operator (%). The modulus operator returns the remainder of a division operation. In this case, it returns the remainder of the division of `n` by 10. This will always be the last digit of `n`.
