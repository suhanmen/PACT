Here is the Python function implemented in a markdown style code block:

```python
def big_diff(lst):
    """
    Write a python function to find the difference between largest and smallest value in a given list.
    """
    return max(lst) - min(lst)

# Test the function
assert big_diff([1,2,3,4]) == 3
```

This function works by using the built-in `max()` and `min()` functions to find the maximum and minimum values in the list, respectively. The difference between these two values is then returned. The `assert` statement is used to test the function with the given example.
