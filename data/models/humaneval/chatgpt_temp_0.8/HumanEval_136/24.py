def largest_smallest_integers(lst):
    # Initialize variables to None
    largest_neg = None
    smallest_pos = None
    
    # Loop through the list
    for num in lst:
        # Check if num is negative and whether it's larger than the current largest_neg
        if num < 0 and (largest_neg is None or num > largest_neg):
            largest_neg = num
        # Check if num is positive and whether it's smaller than the current smallest_pos
        elif num > 0 and (smallest_pos is None or num < smallest_pos):
            smallest_pos = num
    
    # Return the tuple of largest_neg and smallest_pos
    return (largest_neg, smallest_pos)
