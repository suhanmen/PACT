Here is the Python function to find whether the parity of a given number is odd:

```python
def find_Parity(n):
    """
    This function checks if the parity of a given number is odd.
    """
    return n % 2 != 0

# Test the function
assert find_Parity(12) == False
```

In this function, we use the modulus operator (%) to find the remainder of the division of the number by 2. If the remainder is not 0, it means the number is odd, and the function returns True. If the remainder is 0, it means the number is even, and the function returns False.
