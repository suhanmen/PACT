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
    
    # Initialize the output sum to zero
    output = 0
    
    # Iterate through each element in the list
    for num in lst:
        # Round the number up using the ceil() function from the math module
        rounded_num = math.ceil(num)
        # Square the rounded number and add it to the output sum
        output += rounded_num**2
    
    # Return the final output sum
    return output
