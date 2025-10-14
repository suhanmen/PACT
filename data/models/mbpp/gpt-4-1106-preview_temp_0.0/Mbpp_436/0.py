"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""



def neg_nos(numbers):
    return [num for num in numbers if num < 0]

assert neg_nos([-1,4,5,-6]) == [-1,-6]
