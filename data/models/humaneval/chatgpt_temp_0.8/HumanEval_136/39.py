def largest_smallest_integers(lst):
    # Initialize variables to None
    largest_negative = None
    smallest_positive = None
    # Iterate through the list
    for num in lst:
        # Check for negative integers
        if num < 0:
            # If largest_negative is None or less than current number, update it
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        # Check for positive integers
        elif num > 0:
            # If smallest_positive is None or greater than current number, update it
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    # Return a tuple of largest_negative and smallest_positive
    return (largest_negative, smallest_positive)
