def largest_smallest_integers(lst):
    # Initialize variables to hold largest negative and smallest positive integers
    largest_negative = None
    smallest_positive = None
    
    # Iterate through the list
    for num in lst:
        if num < 0:
            # If the number is negative, check if it's the largest negative seen so far
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            # If the number is positive, check if it's the smallest positive seen so far
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    
    # Return the tuple of largest negative and smallest positive integers
    return (largest_negative, smallest_positive)
