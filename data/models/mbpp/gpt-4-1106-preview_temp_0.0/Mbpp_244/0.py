"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""


import math

def next_Perfect_Square(n):
    root = math.ceil(math.sqrt(n))
    return root ** 2

# Example usage:
# result = next_Perfect_Square(35)
# print(result)  # Output: 36
