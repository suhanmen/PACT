"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""



def big_sum(arr):
    if not arr or len(arr) == 0:
        return 0
    min_val = min(arr)
    max_val = max(arr)
    return min_val + max_val

assert big_sum([1,2,3]) == 4
