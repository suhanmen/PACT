Here is the Python function implemented in a markdown style code block:

```python
def Find_Min_Length(list_of_lists):
    """
    Write a python function to find the length of the smallest list in a list of lists.
    """
    return min(len(lst) for lst in list_of_lists)

# Test the function
assert Find_Min_Length([[1],[1,2]]) == 1
```

This function uses a generator expression to calculate the length of each list in the list of lists, and then uses the built-in `min` function to find the smallest length.
