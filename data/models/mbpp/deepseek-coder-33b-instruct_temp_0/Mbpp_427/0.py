Here is the Python function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format:

```python
def change_date_format(date):
    """
    This function converts a date of yyyy-mm-dd format to dd-mm-yyyy format.
    """
    # Split the date string into a list of strings
    date_list = date.split('-')

    # Reverse the list to get the day, month, and year
    reversed_date_list = date_list[::-1]

    # Join the list into a string with '-' as the separator
    new_date = '-'.join(reversed_date_list)

    return new_date

# Test the function
assert change_date_format("2026-01-02") == '02-01-2026'
```

This function works by first splitting the input string into a list of strings using the `split` method. Then it reverses the list to get the day, month, and year in the correct order. Finally, it joins the list into a string with '-' as the separator using the `join` method.
