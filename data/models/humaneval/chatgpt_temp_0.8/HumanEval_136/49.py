def largest_smallest_integers(lst):
    # Initialize variables for largest negative integer and smallest positive integer
    largest_neg = None
    smallest_pos = None
    
    # Loop through the list
    for num in lst:
        # If a negative integer is found, compare it with the current largest negative integer
        if num < 0 and (largest_neg is None or num > largest_neg):
            largest_neg = num
        # If a positive integer is found, compare it with the current smallest positive integer
        elif num > 0 and (smallest_pos is None or num < smallest_pos):
            smallest_pos = num
    
    # Return a tuple of the largest negative integer and smallest positive integer
    return (largest_neg, smallest_pos)
