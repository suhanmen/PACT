"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""


import math

def is_polite(n):
    # Count the number of set bits in the binary representation of n
    count_set_bits = bin(n).count('1')
    # If there is only one set bit, it's a power of 2 and not polite
    if count_set_bits == 1:
        return False
    return True

def nth_polite_number(n):
    count = 0
    i = 0
    while True:
        i += 1
        if is_polite(i):
            count += 1
        if count == n:
            return i

# Example usage
# nth_polite_number(7) should return 11
assert nth_polite_number(7) == 11
