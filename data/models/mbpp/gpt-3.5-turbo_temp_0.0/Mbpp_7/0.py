Here is the completed code snippet:

```python
def find_char_long(string):
    words = string.split()
    long_words = [word for word in words if len(word) >= 4]
    return long_words

assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
```