"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""


import re

def text_lowercase_underscore(s):
    # Regular expression to match sequences of lowercase letters joined with an underscore
    pattern = r'^[a-z]+(_[a-z]+)*$'
    # Search for the pattern in the input string
    return bool(re.match(pattern, s))

# Example usage
# assert text_lowercase_underscore("aab_cbbbc") == (True)
