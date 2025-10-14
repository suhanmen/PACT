Here is the Python function to remove the parenthesis and what is inbetween them from a string:

```python
import re

def remove_parenthesis(s):
    return re.sub(r'\s*\(.*?\)', '', s)

print(remove_parenthesis("python (chrome)"))  # Output: "python"
```

This function uses the `re.sub` function from Python's `re` module to replace all substrings that match the regular expression `\s*\(.*?\)` with an empty string. The regular expression `\s*\(.*?\)` matches any whitespace character (`\s*`), followed by an opening parenthesis (`\(`), followed by any character (`.*?`), followed by a closing parenthesis (`\)`). The `.*?` is a non-greedy match, meaning it will match as few characters as possible.

The `re.sub` function then replaces all matches with an empty string, effectively removing the parentheses and what is inbetween them.
