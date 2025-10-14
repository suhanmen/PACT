"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""


import math

def next_power_of_2(n):
    if n <= 0:
        return 1
    return 2 ** math.ceil(math.log2(n))

# Example usage:
# result = next_power_of_2(0)
# print(result)  # Output: 1
