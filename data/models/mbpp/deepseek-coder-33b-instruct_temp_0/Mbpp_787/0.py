Here is the Python function that matches a string that has an 'a' followed by three 'b':

```python
import re

def text_match_three(text):
    pattern = 'ab{3}$'
    if re.search(pattern,  text):
        return True
    else:
        return False
```

This function uses the `re` module in Python, which provides support for regular expressions. The regular expression `'ab{3}$'` matches any string that ends with 'a' followed by exactly three 'b'. The `$` symbol is an anchor that matches the end of the string.

You can test this function with the following code:

```python
print(text_match_three("ac"))  # False
print(text_match_three("abbb"))  # True
print(text_match_three("abb"))  # False
```

The first call to `text_match_three` returns `False` because the string "ac" does not end with 'a' followed by exactly three 'b'. The second call returns `True` because the string "abbb" does end with 'a' followed by exactly three 'b'. The third call returns `False` because the string "abb" does not end with 'a' followed by exactly three 'b'.
