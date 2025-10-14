Here is the Python function to find the length of the longest word:

```python
def len_log(words):
    """
    This function finds the length of the longest word in a list of words.
    """
    return max(len(word) for word in words)
```

You can test the function with the following code:

```python
assert len_log(["python","PHP","bigdata"]) == 7
```

This function works by using a generator expression to generate the lengths of all words in the list, and then using the built-in `max` function to find the maximum length.
