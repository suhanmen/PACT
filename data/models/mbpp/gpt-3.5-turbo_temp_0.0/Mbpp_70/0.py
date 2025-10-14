Here is the completed code snippet:

```python
def get_equal(tuples):
    lengths = [len(t) for t in tuples]
    return all(length == lengths[0] for length in lengths)
```

This function takes a list of tuples as input and checks if all the tuples have equal length. It does this by first creating a list of the lengths of each tuple using a list comprehension. Then, it uses the `all()` function to check if all the lengths are equal to the length of the first tuple. If they are, it returns `True`, otherwise it returns `False`.