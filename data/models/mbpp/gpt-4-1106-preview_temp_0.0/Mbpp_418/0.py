"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""


def Find_Max(lst):
    return max(lst, key=len)

# Example usage:
# assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
