Here is the Python function that matches a string that has an 'a' followed by anything, ending in 'b'.

```python
import re

def text_starta_endb(s):
    pattern = '^a.*b$'
    if re.search(pattern, s):
        return True
    else:
        return False

# Test the function
print(text_starta_endb("aabbbb"))  # Output: True
```

In this function, we use the `re` module in Python to work with Regular Expressions. The pattern `'^a.*b$'` is used to match a string that starts with 'a' (`^a`), followed by any character (`.*`), and ends with 'b' (`b$`). The `re.search()` function is used to search the string for the pattern. If the pattern is found, the function returns `True`, otherwise it returns `False`.
