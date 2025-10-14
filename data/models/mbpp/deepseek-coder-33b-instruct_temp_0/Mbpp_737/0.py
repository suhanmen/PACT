Here is the Python function implemented in a markdown style code block:

```python
import re

def check_str(s):
    """
    Check if the given string starts with a vowel or not using regex.
    """
    return bool(re.match(r'^[aeiou]', s, re.IGNORECASE))

# Test the function
assert check_str("annie")
```

In this function, we use the `re.match` function to check if the string `s` starts with a vowel. The regular expression `^[aeiou]` matches any string that starts with a vowel (either lowercase or uppercase). The `re.IGNORECASE` flag makes the match case-insensitive. The `bool` function is used to convert the match object to a boolean value (`True` if the string starts with a vowel, `False` otherwise).
