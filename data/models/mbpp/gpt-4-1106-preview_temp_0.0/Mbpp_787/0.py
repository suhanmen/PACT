"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""


import re

def text_match_three(text):
    pattern = 'ab{3}'
    if re.search(pattern, text):
        return True
    else:
        return False

# Test cases
assert not text_match_three("ac")
assert text_match_three("abbb")
assert not text_match_three("abb")
assert not text_match_three("abbbb")
