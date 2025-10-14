"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""


import math

def prime_num(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
# assert prime_num(13) == True
