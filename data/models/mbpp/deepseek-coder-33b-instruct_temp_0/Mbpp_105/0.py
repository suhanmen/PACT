Here is the Python function implemented in a markdown style code block:

```python
def count(lst):
    """
    This function counts the number of True booleans in the given list.
    """
    return lst.count(True)

# Test the function
assert count([True,False,True]) == 2
```

In this function, we use the built-in `count` method of Python lists, which counts the number of occurrences of a specified element in the list. In this case, we are counting the number of `True` elements in the list.
