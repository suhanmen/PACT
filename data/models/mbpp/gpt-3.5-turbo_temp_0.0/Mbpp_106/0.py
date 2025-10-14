Here is the completed code snippet:

```python
def add_lists(lst, tup):
    return tup + tuple(lst)

assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
```

The `add_lists` function takes a list `lst` and a tuple `tup` as input. It appends the elements of the list to the tuple using the `+` operator and returns the resulting tuple. The `assert` statement checks if the function produces the expected output `(9, 10, 5, 6, 7)` and raises an error if it doesn't.