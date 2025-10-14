"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""


import re

def text_match_wordz(text):
    pattern = '.*[zZ].*'
    if re.search(pattern, text):
        return True
    else:
        return False
