"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""


import itertools

def count_Pairs(lst, n):
    # Create all possible pairs using itertools.combinations
    pairs = list(itertools.combinations(lst, 2))
    # Filter out pairs where both elements are unequal
    unequal_pairs = [pair for pair in pairs if pair[0] != pair[1]]
    # Return the number of unequal pairs
    return len(unequal_pairs)

# Example usage:
# assert count_Pairs([1,2,1], 3) == 2
