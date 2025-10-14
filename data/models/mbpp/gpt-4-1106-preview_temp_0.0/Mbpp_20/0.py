"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""


import math

def is_woodall(n):
    if n < 1:
        return False
    k = int(math.log(n + 1, 2))
    return 2**k * k - 1 == n

# Example usage:
# assert is_woodall(383) == True
