def largest_smallest_integers(lst):
    # Initialize the largest negative integer to None
    largest_negative = None
    # Initialize the smallest positive integer to None
    smallest_positive = None
    
    # Loop through each integer in the list
    for integer in lst:
        # Check if the integer is negative
        if integer < 0:
            # If there is no largest negative integer yet, set it as the current integer
            if largest_negative is None:
                largest_negative = integer
            # Otherwise, if the current integer is larger than the current largest negative integer, update it
            elif integer > largest_negative:
                largest_negative = integer
        # Check if the integer is positive
        elif integer > 0:
            # If there is no smallest positive integer yet, set it as the current integer
            if smallest_positive is None:
                smallest_positive = integer
            # Otherwise, if the current integer is smaller than the current 
