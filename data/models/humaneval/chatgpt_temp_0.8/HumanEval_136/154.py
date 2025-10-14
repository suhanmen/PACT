def largest_smallest_integers(lst):
    # Initialize variables for largest negative and smallest positive integers
    largest_negative = None
    smallest_positive = None
    
    # Loop through each number in the list
    for num in lst:
        if num < 0 and (largest_negative is None or num > largest_negative):
            largest_negative = num # Update largest_negative if num is negative and larger than the previous largest_negative
        elif num > 0 and (smallest_positive is None or num < smallest_positive):
            smallest_positive = num # Update smallest_positive if num is positive and smaller than the previous smallest_positive
    
    # Return a tuple of largest_negative and smallest_positive
    return (largest_negative, smallest_positive)
