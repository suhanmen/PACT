"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""



def dict_depth(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(dict_depth(v, level + 1) for k, v in d.items())

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
