"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""


import math

def even_binomial_Coeff_Sum(n):
    sum_even_index = 0
    for i in range(0, n+1, 2):
        sum_even_index += math.comb(n, i)
    return sum_even_index

# Example usage:
# result = even_binomial_Coeff_Sum(4)
# print(result)  # Output: 8
