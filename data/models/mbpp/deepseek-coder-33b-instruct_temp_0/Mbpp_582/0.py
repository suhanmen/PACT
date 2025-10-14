Here is the Python function to check if a dictionary is empty:

```python
def is_dict_empty(dictionary):
    """
    This function checks if a dictionary is empty.
    """
    return not bool(dictionary)
```

You can use this function like this:

```python
my_dict = {10: 'value'}
print(is_dict_empty(my_dict))  # False

empty_dict = {}
print(is_dict_empty(empty_dict))  # True
```

In the first example, the dictionary `my_dict` is not empty, so the function returns `False`. In the second example, the dictionary `empty_dict` is empty, so the function returns `True`.
