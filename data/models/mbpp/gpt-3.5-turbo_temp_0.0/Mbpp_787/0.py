Here is the completed code snippet:

```python
import re

def text_match_three(string):
    pattern = r"ab{3}"
    match = re.search(pattern, string)
    return bool(match)

assert not text_match_three("ac")
```

In this code, we define a function `text_match_three` that takes a string as input. We then define a regular expression pattern `ab{3}` which matches an 'a' followed by three 'b'. We use the `re.search()` function to search for a match of this pattern in the input string. If a match is found, we return `True`, otherwise we return `False`. Finally, we assert that `text_match_three("ac")` returns `False`.