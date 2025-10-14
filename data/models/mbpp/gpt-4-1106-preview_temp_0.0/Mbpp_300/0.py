"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""


import math

def count_binary_seq(n):
    # Calculate the binomial coefficient
    def binomial_coeff(n, k):
        if k == 0 or k == n:
            return 1
        return binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)

    # Calculate the count of binary sequences
    count = 0
    for i in range(n+1):
        count += binomial_coeff(n, i) ** 2
    return count

# Example usage
# count_binary_seq(1) should return 2
