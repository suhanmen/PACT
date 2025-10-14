"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""



def frequency(lst, number):
    return lst.count(number)

assert frequency([1,2,3], 4) == 0
