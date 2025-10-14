python
def double_the_difference(lst):
    # Initialize a variable to store the sum of squares of odd numbers
    sum_of_squares = 0
    
    # Loop through the list
    for num in lst:
        # Ignore negative numbers and non-integers
        if num < 0 or not isinstance(num, int):
            continue
        
        # Check if the number is odd
        if num % 2 == 1:
            # Add the square of the number to the sum
            sum_of_squares += num ** 2
    
    # Double the sum of squares
    sum_of_squares *= 2
    
    # Return the final result
    return sum_of_squares
