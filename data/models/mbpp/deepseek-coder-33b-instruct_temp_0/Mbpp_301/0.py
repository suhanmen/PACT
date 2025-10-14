Here is the Python function to find the depth of a dictionary:

```python
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()), default=0)
    return 0
```

This function works by checking if the input is a dictionary. If it is, it returns 1 plus the maximum depth of its values. If the input is not a dictionary, it returns 0. The `map` function is used to apply the `dict_depth` function to each value in the dictionary, and `max` is used to find the maximum depth. The `default=0` argument to `max` is used to handle the case where the dictionary is empty.

You can test this function with the provided example:

```python
print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))  # Output: 4
```
