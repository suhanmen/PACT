def largest_smallest_integers(lst):
    # Initialize variables to hold largest negative and smallest positive integers
    largest_negative = None
    smallest_positive = None
    
    # Iterate over each element in the list
    for num in lst:
        # Check if the number is negative and update largest_negative if necessary
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        # Check if the number is positive and update smallest_positive if necessary
        elif num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    
    # Return a tuple of the largest negative and smallest positive integers
    return (largest_negative, smallest_positive)
