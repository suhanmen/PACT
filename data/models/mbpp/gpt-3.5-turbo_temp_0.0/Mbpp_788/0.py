Here is the completed code snippet:

```python
def new_tuple(lst, string):
    return tuple(lst + [string])

assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
```

In this code, the `new_tuple` function takes two arguments: `lst` (a list) and `string` (a string). It concatenates the list and the string using the `+` operator and then converts the result into a tuple using the `tuple()` function. Finally, it returns the resulting tuple.

The `assert` statement is used to verify that the function behaves as expected. In this case, it checks if calling `new_tuple(["WEB", "is"], "best")` returns the tuple `('WEB', 'is', 'best')`. If the assertion fails, an `AssertionError` will be raised.