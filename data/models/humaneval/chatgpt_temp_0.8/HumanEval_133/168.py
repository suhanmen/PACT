import math

def sum_squares(lst):
    """
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    """
    
    result = 0
    for num in lst:
        rounded_num = math.ceil(num)
        result += rounded_num**2
    return result
