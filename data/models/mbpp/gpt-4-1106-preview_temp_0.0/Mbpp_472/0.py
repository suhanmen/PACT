"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""


import itertools

def check_Consecutive(lst):
    if len(lst) < 2:
        return False
    sorted_lst = sorted(lst)
    return all(x == y for x, y in itertools.zip_longest(sorted_lst, range(min(sorted_lst), max(sorted_lst) + 1)))

# Example usage
# assert check_Consecutive([1,2,3,4,5]) == True
