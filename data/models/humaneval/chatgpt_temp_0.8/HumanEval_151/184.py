def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    # Initialize the sum of squares to zero
    sum_squares = 0
    
    # Check if the input list is empty
    if not lst:
        return 0
    
    # Iterate through the list and calculate the sum of squares of odd numbers
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 == 1:
            sum_squares += num**2
    
    # Return the doubled sum of squares
    return sum_squares * 2
