"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""


import numpy as np

def max_subarray_product(arr):
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for num in arr[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result

assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
