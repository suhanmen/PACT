Here is the Python function implemented in a markdown style code block:

```python
def find_char_long(s):
    return [word for word in s.split() if len(word) >= 4]

# Test the function
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
```

This function works by splitting the input string into a list of words using the `split()` method, then it checks the length of each word using the `len()` function. If the length of a word is 4 or more characters, it is added to the list. The function finally returns this list.

The test case at the end of the code block checks that the function works correctly by comparing the output of the function to a set of expected output words. If the function works correctly, the `assert` statement will not raise an `AssertionError`.
