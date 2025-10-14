"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""


import re

def text_match_wordz_middle(text):
    pattern = r'\Bz\B'
    if re.search(pattern, text):
        return True
    else:
        return False

# Example usage:
# assert text_match_wordz_middle("pythonzabc.")==True
