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

    # initialize the sum to 0
    sum_of_squares = 0

    # iterate through the list
    for num in lst:
        # ignore negative numbers and non-integers
        if num >= 0 and isinstance(num, int):
            # check if the number is odd
            if num % 2 == 1:
                # add the square of the odd number to the sum
                sum_of_squares += num ** 2

    # double the sum and return it
    return sum_of_squares * 2 if lst else 0
