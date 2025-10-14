def largest_smallest_integers(lst):
    # Initialize variables to track largest negative integer and smallest positive integer
    largest_neg = None
    smallest_pos = None
    
    # Iterate over the list
    for num in lst:
        # If the number is negative and larger than the current largest negative, update largest_neg
        if num < 0 and (largest_neg is None or num > largest_neg):
            largest_neg = num
        # If the number is positive and smaller than the current smallest positive, update smallest_pos
        elif num > 0 and (smallest_pos is None or num < smallest_pos):
            smallest_pos = num
    
    # Return the tuple of largest_neg and smallest_pos
    return (largest_neg, smallest_pos)
