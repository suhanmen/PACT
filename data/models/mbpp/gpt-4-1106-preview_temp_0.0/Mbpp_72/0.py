"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""


import math

def dif_Square(n):
    # A number can be expressed as a difference of two squares
    # if and only if it is not of the form 4k+2 for any integer k.
    # This is because n = x^2 - y^2 = (x + y)(x - y)
    # and for n to be expressible as a difference of two squares,
    # both (x + y) and (x - y) must be integers that differ by an even number.
    # If n is of the form 4k+2, then one of (x + y) or (x - y) would have to be odd,
    # which is not possible.
    return n % 4 != 2

# Example usage:
# assert dif_Square(5) == True
