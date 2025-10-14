"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""


import math

def sum_of_divisors(n):
    total = 1 + n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def are_equivalent(a, b):
    return sum_of_divisors(a) == sum_of_divisors(b)

# Example usage
# assert are_equivalent(36, 57) == False
