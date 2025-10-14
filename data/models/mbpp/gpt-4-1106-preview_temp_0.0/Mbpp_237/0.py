"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""

def check_occurences(tuples_list):
    occurences = {}
    for tup in tuples_list:
        sorted_tup = tuple(sorted(tup))
        occurences[sorted_tup] = occurences.get(sorted_tup, 0) + 1
    return occurences
