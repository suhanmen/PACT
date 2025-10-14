Here is the Python function to count the number of non-empty substrings of a given string:

```python
def number_of_substrings(s):
    n = len(s)
    return n * (n + 1) // 2

# Test the function
assert number_of_substrings("abc") == 6
```

This function works by using the formula for the sum of an arithmetic series. The number of substrings of a string of length `n` is `n * (n + 1) / 2`. This formula is derived from the fact that each character in the string can be the start of `n - i + 1` substrings, where `i` is the index of the character in the string.
