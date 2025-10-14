"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""



def empty_dict(dicts):
    return all(not d for d in dicts)

assert empty_dict([{}, {}, {}]) == True
