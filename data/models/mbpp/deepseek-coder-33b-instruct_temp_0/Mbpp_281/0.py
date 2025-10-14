Here is the Python function implemented in a markdown style code block:

```python
def all_unique(lst):
    """
    This function checks if all elements in a list are unique.
    """
    if len(lst) == len(set(lst)):
        return True
    else:
        return False
```

You can use this function to check if all elements in a list are unique. The function works by converting the list to a set, which automatically removes any duplicate elements. If the length of the list is equal to the length of the set, it means all elements are unique and the function returns True. Otherwise, it returns False.
