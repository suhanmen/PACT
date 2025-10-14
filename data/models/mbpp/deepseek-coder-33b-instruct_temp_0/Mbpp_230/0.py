Here is the Python function implemented in a markdown style code block:

```python
def replace_blank(string, char):
    return string.replace(' ', char)

# Test the function
assert replace_blank("hello people",'@')==("hello@people")
```

This function works by using the `replace` method of the string object in Python, which replaces all occurrences of a specified character (in this case, a blank space) with another specified character (the `char` argument). The `assert` statement is used to test the function. If the function is implemented correctly, the `assert` statement will not raise an `AssertionError`, indicating that the function is working as expected.
