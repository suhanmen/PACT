Here is the Python function implemented in a markdown style code block:

```python
def sum_digits(n):
    """
    Write a function to get the sum of the digits of a non-negative integer.
    """
    return sum(int(digit) for digit in str(n))

# Test the function
assert sum_digits(345)==12
```

This function works by converting the integer to a string, then iterating over each character in the string (which are the digits of the original number). It converts each character back to an integer and adds it to the sum.
