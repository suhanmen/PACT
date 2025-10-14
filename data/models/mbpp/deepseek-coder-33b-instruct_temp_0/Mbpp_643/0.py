Here is the Python function that checks if a string contains 'z', except at the start and end of the word:

```python
def text_match_wordz_middle(s):
    return s[1:-1].find('z') != -1

# Test the function
print(text_match_wordz_middle("pythonzabc."))  # Output: True
```

In this function, we use Python's string slicing to exclude the first and last characters of the string. Then we use the `find` method to check if 'z' is present in the middle of the string. If 'z' is found, `find` returns the index of its first occurrence, otherwise it returns -1. Therefore, we return `True` if 'z' is found and `False` otherwise.
