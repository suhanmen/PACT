Here is the Python function that solves the problem:

```python
def add_dict_to_tuple(tup, dictionary):
    return tup + (dictionary,)
```

You can test the function with the provided example:

```python
print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))
```

This should output: `(4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})`.
