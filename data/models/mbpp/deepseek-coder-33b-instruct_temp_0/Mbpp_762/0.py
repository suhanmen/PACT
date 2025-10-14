Here is the Python function implemented in a markdown style code block:

```python
def check_monthnumber_number(month_number):
    """
    This function checks whether the given month number contains 30 days or not.
    Months are given as number from 1 to 12.
    """
    # List of months with 30 days
    thirty_days_months = [4, 6, 9, 11]

    # Check if the month number is in the list of months with 30 days
    if month_number in thirty_days_months:
        return True
    else:
        return False

# Test the function
assert check_monthnumber_number(6)==True
```

In this function, we first define a list of months that have 30 days. Then, we check if the input month number is in this list. If it is, the function returns `True`, otherwise it returns `False`.
