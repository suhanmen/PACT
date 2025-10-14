"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""



def max_product_tuple(pairs):
    return max(abs(a * b) for a, b in pairs)

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
