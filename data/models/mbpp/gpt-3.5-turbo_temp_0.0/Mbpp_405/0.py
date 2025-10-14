Here is the completed code snippet:

```python
def check_tuplex(tup, element):
    return element in tup

assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
```

In this code, the `check_tuplex` function takes in a tuple `tup` and an `element` to check. It uses the `in` operator to check if the `element` exists within the `tup`. The function returns `True` if the element is found, and `False` otherwise.

The `assert` statement is used to verify that the function works as expected. It checks if the result of `check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r')` is equal to `True`. If the result is not `True`, an `AssertionError` will be raised.