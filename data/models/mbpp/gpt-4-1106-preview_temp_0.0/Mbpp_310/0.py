"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""


def string_to_tuple(input_string):
    return tuple(input_string)

assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')
