"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""


import math

def zero_count(arr):
    if not arr:
        return 0
    zero_count = arr.count(0)
    non_zero_count = len(arr) - zero_count
    if non_zero_count == 0:
        return float('inf')
    return zero_count / non_zero_count

# Example usage:
# ratio = zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
# print(ratio)
