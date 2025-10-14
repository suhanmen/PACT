import math

def sum_squares(lst):
    # Initialize a variable to keep track of the sum of squared numbers
    sum_of_squares = 0
    
    # Loop through each element in the list
    for num in lst:
        # Round the number to the nearest upper integer
        num = math.ceil(num)
        # Square the number and add it to the sum_of_squares variable
        sum_of_squares += num**2
    
    # Return the final sum_of_squares value
    return sum_of_squares
