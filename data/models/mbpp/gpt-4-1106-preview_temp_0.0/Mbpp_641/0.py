"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""


import math

def is_nonagonal(n):
    # The formula for the nth nonagonal number is: n(7n-5)/2
    return n * (7 * n - 5) // 2

# Example usage
# To find the 10th nonagonal number
nonagonal_number_10 = is_nonagonal(10)
print(f'The 10th nonagonal number is: {nonagonal_number_10}')

# Assertion
assert is_nonagonal(10) == 325
