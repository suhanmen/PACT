Here is the Python function implemented in a markdown style code block:

```python
def check_smaller(tuple1, tuple2):
    for i in range(len(tuple1)):
        if tuple1[i] <= tuple2[i]:
            return False
    return True
```

This function iterates over each element in the first tuple and checks if it is smaller than or equal to the corresponding element in the second tuple. If it finds an element in the first tuple that is not smaller than the corresponding element in the second tuple, it immediately returns `False`. If it goes through all elements without finding such an element, it returns `True`.
