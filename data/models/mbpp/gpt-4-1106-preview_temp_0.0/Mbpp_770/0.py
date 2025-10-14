"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""



def odd_num_sum(n):
    return sum([i**4 for i in range(1, 2*n, 2)])

assert odd_num_sum(2) == 82
