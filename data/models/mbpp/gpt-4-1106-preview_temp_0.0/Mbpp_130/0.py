"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""


import collections

def max_occurrences(lst):
    # Create a counter object to count the frequency of each item
    counter = collections.Counter(lst)
    # Find the item with the maximum frequency
    max_occurrence_item = max(counter, key=counter.get)
    return max_occurrence_item

# Example usage
# assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2
