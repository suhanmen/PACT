Here is the completed code snippet:

```python
def add_tuple(lst, tup):
    return lst + list(tup)

assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
```

In this code, the `add_tuple` function takes two parameters: `lst` (the list to which the tuple will be added) and `tup` (the tuple to be added). The function uses the `+` operator to concatenate the list and the converted tuple (using the `list()` function). The result is then returned.

The `assert` statement is used to verify that the function behaves as expected. It checks if the result of calling `add_tuple([5, 6, 7], (9, 10))` is equal to `[5, 6, 7, 9, 10]`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.