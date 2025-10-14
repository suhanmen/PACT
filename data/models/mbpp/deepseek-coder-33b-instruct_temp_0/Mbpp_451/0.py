Here is the Python function to remove all whitespaces from the given string:

```python
def remove_whitespaces(s):
    return s.replace(" ", "")

# Test the function
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
```

This function uses the `replace` method of the string class to replace all spaces with no space, effectively removing all whitespaces from the string.
