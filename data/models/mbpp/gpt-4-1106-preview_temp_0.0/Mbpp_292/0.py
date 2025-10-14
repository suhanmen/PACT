"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""


import math

def find(numerator, denominator):
    if denominator == 0:
        raise ValueError('Cannot divide by zero')
    return math.floor(numerator / denominator)

# Example usage:
# quotient = find(10, 3)
# print(quotient)  # Output: 3

# Test case
assert find(10, 3) == 3
