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
    
    # Initialize a variable to hold the sum of the squared numbers
    sum_of_squares = 0
    
    # Loop through each element in the list
    for num in lst:
        
        # Round the number up to the nearest integer (ceiling)
        num = int(num + (1 if num > 0 else 0))
        
        # Square the number and add it to the sum_of_squares variable
        sum_of_squares += num**2
    
    # Return the sum of squared numbers
    return sum_of_squares
