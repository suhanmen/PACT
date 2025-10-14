"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""


import re

def text_match_two_three(text):
    pattern = 'ab{2,3}'
    if re.search(pattern, text):
        return True
    return False

# Example usage:
# assert text_match_two_three("ac") == (False)
