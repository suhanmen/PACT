Here is the completed code snippet:

```python
def opposite_Signs(a, b):
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return True
    else:
        return False

assert opposite_Signs(1, -2) == True
```

In this code, the `opposite_Signs` function takes two integers `a` and `b` as input. It checks if one of the integers is negative and the other is positive, or vice versa. If this condition is true, it returns `True`, indicating that the integers have opposite signs. Otherwise, it returns `False`.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `opposite_Signs(1, -2)` returns `True`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.