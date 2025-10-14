Here is the Python function implemented in a markdown style code block:

```python
def add_lists(lst, tup):
    """
    Write a function to append the given list to the given tuples.
    """
    return tup + tuple(lst)

# Test the function
print(add_lists([5, 6, 7], (9, 10)))  # Output: (9, 10, 5, 6, 7)
```

This function takes a list and a tuple as input, converts the list to a tuple, and then concatenates the two tuples. The result is a new tuple that includes all elements from the original tuple followed by all elements from the list.
