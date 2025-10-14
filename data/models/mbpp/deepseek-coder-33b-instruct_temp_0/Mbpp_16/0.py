Here is the Python function implemented in a markdown style code block:

```python
import re

def text_lowercase_underscore(text):
    """
    This function checks if the input string contains sequences of lowercase letters joined with an underscore.
    """
    pattern = r'^[a-z]+(_[a-z]+)*$'
    return bool(re.match(pattern, text))

# Test the function
print(text_lowercase_underscore("aab_cbbbc"))  # Expected output: True
```

In this function, we use a regular expression to check if the input string matches the pattern of one or more lowercase letters followed by an underscore and another sequence of lowercase letters. The `^` and `$` symbols are used to denote the start and end of the string, respectively. The `*` symbol is used to denote zero or more of the preceding element. The `+` symbol is used to denote one or more of the preceding element. The `bool()` function is used to convert the result of `re.match()` to a boolean value.
