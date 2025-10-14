"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""


import math

def sum_of_common_divisors(a, b):
    def common_divisors(n1, n2):
        divisors = []
        for i in range(1, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0:
                divisors.append(i)
        return divisors
    
    return sum(common_divisors(a, b))

# Example usage:
# assert sum_of_common_divisors(10, 15) == 6
