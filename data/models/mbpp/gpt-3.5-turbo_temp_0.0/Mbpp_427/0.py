Here's the completed code snippet:

```python
def change_date_format(date):
    # Split the date string into year, month, and day
    year, month, day = date.split('-')
    
    # Concatenate the day, month, and year with '-' as the separator
    new_date = f"{day}-{month}-{year}"
    
    return new_date

# Test the function
assert change_date_format("2026-01-02") == '02-01-2026'
```