Here is the Python function implemented in a markdown style code block:

```python
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```

This function iterates over the list, checking every even indexed element. If it finds an odd number, it immediately returns `False`. If it doesn't find any odd numbers, it returns `True`.
