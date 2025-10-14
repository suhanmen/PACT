"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""


import itertools

def combinations_colors(colors, n):
    return list(itertools.product(colors, repeat=n))

# Example usage:
# assert combinations_colors(['Red', 'Green', 'Blue'], 1) == [('Red',), ('Green',), ('Blue',)]
