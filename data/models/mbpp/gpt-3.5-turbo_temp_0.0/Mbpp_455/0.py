Here is the completed code snippet:

```python
def check_monthnumb_number(month):
    thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
    if month in thirty_one_days:
        return True
    else:
        return False

assert check_monthnumb_number(5) == True
```

In this code, we define a function `check_monthnumb_number` that takes a `month` parameter. We create a list `thirty_one_days` that contains the month numbers that have 31 days. We then check if the given `month` is in the `thirty_one_days` list. If it is, we return `True`, indicating that the month has 31 days. Otherwise, we return `False`. Finally, we use an `assert` statement to verify that `check_monthnumb_number(5)` returns `True`.