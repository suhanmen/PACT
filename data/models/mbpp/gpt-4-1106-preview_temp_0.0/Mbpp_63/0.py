"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""



def max_difference(pairs):
    return max(abs(x - y) for x, y in pairs)

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
