Here is the Python function to remove lowercase substrings from a given string:

```python
def remove_lowercase(s):
    return ''.join(c for c in s if c.isupper())

print(remove_lowercase("PYTHon"))  # Output: PYTH
```

This function works by iterating over each character in the string `s`. If the character is uppercase (as determined by the `isupper()` method), it is included in the output string. The `join()` method is used to concatenate all the uppercase characters into a single string.
