Here is the Python function implemented in a markdown style code block:

```python
def remove_dirty_chars(s1, s2):
    """
    Write a function to remove characters from the first string which are present in the second string.
    """
    return ''.join([c for c in s1 if c not in s2])

# Test the function
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
```

This function works by iterating over each character in the first string (`s1`). If the character is not in the second string (`s2`), it is included in the result. The `join` function is used to combine the remaining characters into a single string.
