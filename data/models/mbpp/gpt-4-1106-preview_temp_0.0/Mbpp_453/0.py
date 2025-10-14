"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""



def sumofFactors(n):
    sum_even_factors = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            sum_even_factors += i
    return sum_even_factors

# Example usage:
# result = sumofFactors(18)
# print(result)  # Output will be 26

# Test the function
assert sumofFactors(18) == 26
