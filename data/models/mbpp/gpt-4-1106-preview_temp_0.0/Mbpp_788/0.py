"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""


def new_tuple(lst, string):
    return tuple(lst) + (string,)

# Example usage
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
