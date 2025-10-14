Here is the Python function to drop empty items from a given dictionary:

```python
def drop_empty(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}
```

This function uses a dictionary comprehension to create a new dictionary that only includes items from the original dictionary where the value is not None.
