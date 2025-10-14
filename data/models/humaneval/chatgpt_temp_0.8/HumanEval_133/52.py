import math

def sum_squares(lst):
    """
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    """
    sum_of_squares = 0
    for num in lst:
        num = math.ceil(num)
        sum_of_squares += num**2
    return sum_of_squares
