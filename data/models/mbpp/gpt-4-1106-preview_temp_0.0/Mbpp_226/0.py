"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""



def odd_values_string(s):
    return s[::2]


assert odd_values_string('abcdef') == 'ace'
