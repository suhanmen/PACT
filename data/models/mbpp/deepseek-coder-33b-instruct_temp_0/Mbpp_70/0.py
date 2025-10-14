Here is the Python function implemented in a markdown style code block:

```python
def get_equal(tuples):
    """
    Write a function to find whether all the given tuples have equal length or not.
    """
    return len(set(len(t) for t in tuples)) == 1

# Test the function
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
```

This function works by creating a set of the lengths of the tuples. If all tuples have the same length, the set will only contain one element. Therefore, if the length of the set is 1, the function returns True, otherwise it returns False.
