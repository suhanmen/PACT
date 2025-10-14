"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""



def string_to_list(input_string):
    return input_string.split(' ')

assert string_to_list("python programming")==['python','programming']
