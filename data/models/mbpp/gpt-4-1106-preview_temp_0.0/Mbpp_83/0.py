"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""


import string

def get_Char(s):
    total_ascii = sum(ord(char) for char in s)
    return string.ascii_lowercase[total_ascii % 26]

assert get_Char("abc") == "f"
