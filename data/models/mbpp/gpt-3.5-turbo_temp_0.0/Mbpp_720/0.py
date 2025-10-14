Here is the completed code snippet:

```python
def add_dict_to_tuple(tup, dictionary):
    return tup + (dictionary,)

assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
```

The `add_dict_to_tuple` function takes in a tuple `tup` and a dictionary `dictionary`. It concatenates the tuple with the dictionary using the `+` operator and returns the resulting tuple. The `assert` statement checks if the function produces the expected output.