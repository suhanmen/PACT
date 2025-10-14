"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""


import re

def is_decimal(num_str):
    # Regular expression to match a decimal number with a precision of 2
    pattern = r'^\d+(\.\d{2})?$'
    return bool(re.match(pattern, num_str))

# Example usage
# assert is_decimal('123.11') == True
