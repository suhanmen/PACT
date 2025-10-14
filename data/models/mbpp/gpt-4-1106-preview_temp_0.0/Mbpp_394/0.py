"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""



def check_distinct(tpl):
    return len(tpl) == len(set(tpl))

assert check_distinct((1, 4, 5, 6, 1, 4)) == False
