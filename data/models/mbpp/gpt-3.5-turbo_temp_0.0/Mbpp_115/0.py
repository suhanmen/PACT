Here is the completed code snippet:

```python
def empty_dict(lst):
    for d in lst:
        if d:
            return False
    return True

assert empty_dict([{},{},{}]) == True
```