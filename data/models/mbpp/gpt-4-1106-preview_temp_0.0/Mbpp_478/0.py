"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""



def remove_lowercase(input_string):
    return ''.join(filter(str.isupper, input_string))

# Example usage
assert remove_lowercase("PYTHon") == 'PYTH'
