"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""


import math

def is_perfect_square(number):
    if number < 0:
        return False
    root = math.isqrt(number)
    return number == root * root

assert not is_perfect_square(10)
