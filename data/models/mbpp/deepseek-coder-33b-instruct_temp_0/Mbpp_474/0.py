Here is the Python function to replace characters in a string:

```python
def replace_char(s, old, new):
    return s.replace(old, new)

# Test the function
print(replace_char("polygon",'y','l'))
```

This function uses the built-in `replace()` method of Python strings, which replaces all occurrences of a specified character with another specified character. The `replace()` method returns a new string where some specified values are replaced with other specified values.

In the test, the function is called with the string "polygon", the character to be replaced ('y') and the character to replace it with ('l'). The function should return the string "pollgon".
