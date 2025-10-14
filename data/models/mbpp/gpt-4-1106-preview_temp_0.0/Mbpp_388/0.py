"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""


import math

def highest_Power_of_2(n):
    # Find the highest power of 2 less than or equal to n
    return 2 ** int(math.log(n, 2))

# Example usage
# assert highest_Power_of_2(10) == 8
