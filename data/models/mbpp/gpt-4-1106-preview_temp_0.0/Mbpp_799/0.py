"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""


import ctypes

def left_rotate(n, d):
    # Assuming n is a 32-bit integer
    INT_BITS = 32
    # Left rotate the bits
    return (n << d)|(n >> (INT_BITS - d)) & 0xFFFFFFFF

# Test
assert left_rotate(16,2) == 64
