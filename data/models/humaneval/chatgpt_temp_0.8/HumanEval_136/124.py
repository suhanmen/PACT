def largest_smallest_integers(lst):
    # Initialize variables to hold largest negative integer and smallest positive integer
    largest_negative = None
    smallest_positive = None
    
    # Loop through the list
    for num in lst:
        if num < 0:  # If the number is negative
            if largest_negative is None or num > largest_negative:  # Check if it's the largest negative found so far
                largest_negative = num
        elif num > 0:  # If the number is positive
            if smallest_positive is None or num < smallest_positive:  # Check if it's the smallest positive found so far
                smallest_positive = num
    
    # Return the tuple of largest negative and smallest positive integers
    return (largest_negative, smallest_positive)
