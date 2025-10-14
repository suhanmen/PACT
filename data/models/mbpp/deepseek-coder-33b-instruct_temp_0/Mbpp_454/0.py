Here is the Python function that matches a word containing 'z' in a markdown style code block:

```python
import re

def text_match_wordz(text):
    pattern = '\\b\\w*z\\w*\\b'
    if re.search(pattern,  text):
        return True
    else:
        return False

# Test the function
print(text_match_wordz("pythonz."))  # Output: True
```

In this function, we use the `re` module to use regular expressions. The pattern `\\b\\w*z\\w*\\b` matches any word that contains 'z'. The `\\b` is a word boundary, `\\w*` matches any word character (equal to [a-zA-Z0-9_]) between zero and unlimited times.

The `re.search` function searches the string for a match to the pattern, returning a match object, or `None` if no match was found. If a match is found, the function returns `True`, otherwise it returns `False`.
