"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""



def count(bool_list):
    return sum(1 for item in bool_list if item is True)

# Example usage:
# assert count([True, False, True]) == 2
