Here is the Python function implemented in a markdown style code block:

```python
def check_char(s):
    if s[0] == s[-1]:
        return "Valid"
    else:
        return "Invalid"

# Test the function
print(check_char("abba"))  # Output: Valid
```

This function works by comparing the first character of the string (`s[0]`) with the last character of the string (`s[-1]`). If they are the same, it returns "Valid", otherwise it returns "Invalid".
