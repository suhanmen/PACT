Here is the completed code snippet:

```python
def list_tuple(lst):
    return tuple(lst)

assert list_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)
```

The `list_tuple` function takes a list as input and uses the `tuple` function to convert it into a tuple. The `assert` statement checks if the output of `list_tuple([5, 10, 7, 4, 15, 3])` is equal to `(5, 10, 7, 4, 15, 3)`.