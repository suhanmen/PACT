Here is the completed code snippet:

```python
def dict_depth(dictionary):
    if not isinstance(dictionary, dict):
        return 0
    if not dictionary:
        return 1
    return 1 + max(dict_depth(value) for value in dictionary.values())

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
```

The `dict_depth` function takes a dictionary as input and recursively calculates the depth of the dictionary. It checks if the input is a dictionary and if it is empty. If the input is not a dictionary, it returns 0. If the input is an empty dictionary, it returns 1. Otherwise, it recursively calls `dict_depth` on each value in the dictionary and returns the maximum depth found, incremented by 1.