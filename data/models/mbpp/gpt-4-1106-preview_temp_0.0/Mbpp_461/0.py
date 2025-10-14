"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""



def upper_ctr(s):
    return sum(1 for char in s if char.isupper())

assert upper_ctr('PYthon') == 2
