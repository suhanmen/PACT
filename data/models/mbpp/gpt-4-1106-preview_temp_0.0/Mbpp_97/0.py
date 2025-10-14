"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

from collections import Counter

def frequency_lists(list_of_lists):
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    return dict(Counter(flattened_list))
