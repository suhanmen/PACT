Here is the completed code snippet:

```python
def text_lowercase_underscore(text):
    # Check if the input string contains sequences of lowercase letters joined with an underscore
    if "_" in text:
        parts = text.split("_")
        for part in parts:
            if not part.islower():
                return False
        return True
    else:
        return False

# Test the function
assert text_lowercase_underscore("aab_cbbbc") == True
```

The function `text_lowercase_underscore` takes a string `text` as input and checks if it contains sequences of lowercase letters joined with an underscore. It returns `True` if the condition is met, and `False` otherwise. In the provided example, the input string "aab_cbbbc" contains lowercase sequences "aab" and "cbbbc" joined with an underscore, so the function should return `True`.