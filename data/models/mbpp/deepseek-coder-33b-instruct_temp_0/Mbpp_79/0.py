Here is the Python function implemented in a markdown style code block:

```python
def word_len(word):
    """
    This function checks whether the length of the word is odd or not.
    """
    return len(word) % 2 != 0

# Test the function
assert word_len("Hadoop") == False
```

In this function, the `len()` function is used to get the length of the word. The modulus operator `%` is used to check if the length of the word is odd. If the length of the word is odd, the function will return `True`, otherwise it will return `False`.
