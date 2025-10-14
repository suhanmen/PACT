"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""


import itertools

def get_ludic(n):
    ludic = [1]
    candidates = list(range(2, n + 1))
    while candidates:
        first = candidates[0]
        ludic.append(first)
        candidates = [c for i, c in enumerate(candidates) if (i + 1) % first != 0]
    return ludic

# Example usage
# print(get_ludic(10))
