"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""


import re

def change_date_format(date_str):
    # Check if the input date_str matches the yyyy-mm-dd format
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        # Split the date by '-' and reverse the components
        parts = date_str.split('-')
        return '-'.join(parts[::-1])
    else:
        raise ValueError('Invalid date format. Please use yyyy-mm-dd format.')

# Example usage:
# assert change_date_format("2026-01-02") == '02-01-2026'
