"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""



def min_product_tuple(pairs):
    return min(a * b for a, b in pairs)

assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
