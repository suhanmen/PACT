Here is the completed code snippet:

```python
import re

def text_starta_endb(text):
    pattern = r'a.*b$'
    if re.match(pattern, text):
        return True
    else:
        return False

assert text_starta_endb("aabbbb")
```

In this code, we use the `re` module to perform regular expression matching. The regular expression pattern `a.*b$` matches a string that starts with an 'a', followed by any number of characters (denoted by `.*`), and ends with a 'b'. The `re.match()` function is used to check if the given `text` matches the pattern. If it does, the function returns `True`, otherwise it returns `False`. The `assert` statement is used to verify that the function returns `True` for the given test case.