"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""


import functools

def find_lucas(n):
    @functools.lru_cache(maxsize=None)
    def lucas_number(n):
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return lucas_number(n - 1) + lucas_number(n - 2)
    return lucas_number(n)

assert find_lucas(9) == 76
