Here is the Python function implemented in a markdown style code block:

```python
def upper_ctr(s):
    """
    Write a python function to count the upper case characters in a given string.
    """
    return sum(1 for c in s if c.isupper())

# Test the function
assert upper_ctr('PYthon') == 1
```

This function works by iterating over each character in the string `s`. If the character is an uppercase letter (as determined by the `isupper()` method), it adds 1 to the sum. The `sum()` function then adds up all the 1s to give the total count of uppercase letters.
