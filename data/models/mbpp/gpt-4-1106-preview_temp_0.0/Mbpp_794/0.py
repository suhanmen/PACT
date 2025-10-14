"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""


import re

def text_starta_endb(s):
    pattern = '^a.*b$'
    if re.search(pattern, s):
        return True
    else:
        return False

assert text_starta_endb("aabbbb")
