Here is the Python function implemented in a markdown style code block:

```python
def check_distinct(tup):
    """
    Write a function to check if given tuple contains no duplicates.
    """
    return len(tup) == len(set(tup))

# Test the function
print(check_distinct((1, 4, 5, 6, 1, 4)))  # Output: False
```

In this function, we are converting the tuple to a set. In Python, a set is an unordered collection of unique elements. If the length of the set is equal to the length of the tuple, it means there are no duplicates in the tuple. If the lengths are not equal, it means there are duplicates in the tuple.
