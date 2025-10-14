"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""


import math

def is_not_prime(n):
    if n <= 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

# Example usage:
# print(is_not_prime(2))  # Output: False
