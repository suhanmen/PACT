"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""



def tup_string(tup):
    return ''.join(tup)

assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"
