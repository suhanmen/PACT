Here is the completed code snippet:

```python
def check_type(tup):
    return len(set(map(type, tup))) == 1

assert check_type((5, 6, 7, 3, 5, 6)) == True
```

In this code, the `check_type` function takes a tuple as input. It uses the `map` function to apply the `type` function to each element of the tuple. The resulting types are then converted to a set to remove duplicates. If the length of the set is 1, it means all elements have the same data type, so the function returns `True`. Otherwise, it returns `False`.

The `assert` statement is used to verify that the function behaves as expected. In this case, it checks that `check_type((5, 6, 7, 3, 5, 6))` returns `True`.