import math

def sum_squares(lst):
    """
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    """
    sum_squared = 0
    for num in lst:
        ceil_num = math.ceil(num)
        sum_squared += ceil_num**2
    return sum_squared
