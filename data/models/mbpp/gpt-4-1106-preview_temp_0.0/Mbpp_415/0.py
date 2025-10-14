"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""


import itertools

def max_Product(arr):
    if len(arr) < 2:
        return None
    max_product = float('-inf')
    max_pair = ()
    for pair in itertools.combinations(arr, 2):
        product = pair[0] * pair[1]
        if product > max_product:
            max_product = product
            max_pair = pair
    return max_pair

# Example usage
# assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
