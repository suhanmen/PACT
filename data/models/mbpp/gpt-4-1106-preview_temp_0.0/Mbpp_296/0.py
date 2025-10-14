"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""


import itertools

def get_Inv_Count(arr):
    return sum(1 for i, j in itertools.combinations(range(len(arr)), 2) if arr[i] > arr[j])

# Example usage
# assert get_Inv_Count([1,20,6,4,5]) == 5
