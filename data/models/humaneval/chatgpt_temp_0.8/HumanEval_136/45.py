def largest_smallest_integers(lst):
    # Initialize variables for largest negative and smallest positive integers
    largest_negative = None
    smallest_positive = None
    
    # Loop through the list to find largest negative and smallest positive integers
    for num in lst:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    
    # Return a tuple of largest_negative and smallest_positive integers
    return (largest_negative, smallest_positive)
