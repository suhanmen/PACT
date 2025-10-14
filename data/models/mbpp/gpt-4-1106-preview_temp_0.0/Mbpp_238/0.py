"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""



def number_of_substrings(s):
    length = len(s)
    return (length * (length + 1)) // 2

assert number_of_substrings("abc") == 6
