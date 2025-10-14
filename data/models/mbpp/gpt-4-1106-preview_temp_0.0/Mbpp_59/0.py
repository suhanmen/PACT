"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""



def is_octagonal(n):
    return n * (3 * n - 2)

assert is_octagonal(5) == 65
