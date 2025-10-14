"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""


import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def sum_Of_product(n):
    sum_product = 0
    for i in range(n):
        sum_product += binomial_coefficient(n, i) * binomial_coefficient(n, i + 1)
    return sum_product

# Example usage:
# assert sum_Of_product(3) == 15
