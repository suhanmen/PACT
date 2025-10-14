"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""


import itertools

def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    for r in range(1, len(lst) + 1):
        for sub in itertools.combinations(lst, r):
            prod = 1
            for num in sub:
                prod *= num
            total_sum += prod
    return total_sum

assert sum_Of_Subarray_Prod([1,2,3]) == 20
