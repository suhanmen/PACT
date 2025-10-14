Here is the Python function implemented in a markdown style code block:

```python
def odd_position(lst):
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            return False
    return True
```

This function iterates over the list and checks if the index is odd (`i % 2 != 0`) and the corresponding element is even (`lst[i] % 2 == 0`). If it finds such a pair, it immediately returns `False`. If it doesn't find any such pair after checking all elements, it returns `True`.
