"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""



def sum_negativenum(numbers):
    return sum(filter(lambda x: x < 0, numbers))

assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
