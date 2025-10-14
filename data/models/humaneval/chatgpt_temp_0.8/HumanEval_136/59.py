def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    # Initialize variables for largest negative integer and smallest positive integer
    largest_neg = None
    smallest_pos = None
    
    # Loop through the list, checking for negative and positive integers
    for num in lst:
        if num < 0:
            if largest_neg is None or num > largest_neg:
                largest_neg = num
        elif num > 0:
            if smallest_pos is None or num < smallest_pos:
                smallest_pos = num
    
    # Return the tuple of largest negative and smallest positive integers
    return (largest_neg, smallest_pos)
