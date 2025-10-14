import math

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    
    # First, round each element in the list to the upper int (ceiling)
    rounded_lst = [math.ceil(num) for num in lst]
    
    # Then, square each element and add them up
    sum_squares = sum([num**2 for num in rounded_lst])
    
    return sum_squares
