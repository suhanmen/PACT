Here is the Python function implemented in a markdown style code block:

```python
def empty_dict(list_of_dicts):
    """
    This function checks whether all dictionaries in a list are empty or not.
    """
    return all(not d for d in list_of_dicts)
```

You can use this function like this:

```python
print(empty_dict([{},{},{}]))  # Output: True
```

This function works by using the `all` function in Python, which returns `True` if all elements in the iterable (in this case, the list of dictionaries) are `True`. The `not d` expression checks if the dictionary `d` is empty. If all dictionaries are empty, `all(not d for d in list_of_dicts)` will return `True`, otherwise it will return `False`.
