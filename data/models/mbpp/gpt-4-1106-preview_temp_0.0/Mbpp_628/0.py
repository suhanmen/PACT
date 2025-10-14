"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""



def replace_spaces(input_string):
    return input_string.replace(' ', '%20')

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
