Here is the Python function implemented in a markdown style code block:

```python
def check_month_number(month_number):
    """
    Write a function to check whether the given month number contains 31 days or not.
    """
    # List of months with 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

    # Check if the month number is in the list
    if month_number in months_with_31_days:
        return True
    else:
        return False

# Test the function
assert check_month_number(5) == True
```

This function works by creating a list of the months that have 31 days. It then checks if the input month number is in this list. If it is, the function returns `True`, otherwise it returns `False`. The test at the end of the code block checks that the function works correctly for the month of May (month number 5).
