"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""


import math

def catalan_number(n):
    # Using the Binomial Coefficient
    # Catalan(n) = (2n)! / ((n+1)! * n!)
    return math.comb(2*n, n) // (n+1)

# Example usage
# print(catalan_number(10))
