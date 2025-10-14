Here is the completed code snippet:

```python
def check_monthnumber_number(month):
    if month in [4, 6, 9, 11]:
        return True
    else:
        return False

assert check_monthnumber_number(6)==True
```

In this code, the function `check_monthnumber_number` takes a month number as input and checks if it corresponds to a month with 30 days. If the month number is 4, 6, 9, or 11, the function returns `True`, indicating that the month has 30 days. Otherwise, it returns `False`. The `assert` statement is used to verify that the function returns the expected result for the given test case.