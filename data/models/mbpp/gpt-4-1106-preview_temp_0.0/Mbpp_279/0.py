"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""


import math

def is_num_decagonal(n):
    if n < 1:
        return False
    # The formula for the nth decagonal number is: Dn = 4n^2 - 3n
    decagonal_number = 4 * n**2 - 3 * n
    return decagonal_number

# Example usage:
# decagonal_number = is_num_decagonal(3)
# print(decagonal_number)  # Output should be 27
