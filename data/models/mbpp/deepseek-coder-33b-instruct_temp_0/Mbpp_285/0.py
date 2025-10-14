Here is the Python function implemented in a markdown style code block:

```python
import re

def text_match_two_three(string):
    pattern = 'ab{2,3}'
    if re.search(pattern, string):
        return True
    else:
        return False

# Test the function
print(text_match_two_three("ac")) # Expected output: False
```

This function uses the `re` module in Python, which provides support for regular expressions. The regular expression `'ab{2,3}'` matches any string that contains 'a' followed by two or three 'b' characters. The `re.search()` function is used to search the string for the pattern. If the pattern is found, the function returns `True`, otherwise it returns `False`.
