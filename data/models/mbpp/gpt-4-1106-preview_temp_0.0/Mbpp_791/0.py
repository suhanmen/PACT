"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""



def remove_nested(tpl):
    return tuple(item for item in tpl if not isinstance(item, tuple))

assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
