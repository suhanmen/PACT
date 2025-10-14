def largest_smallest_integers(lst):
    # Initialize variables to store largest negative integer and smallest positive integer
    largest_negative = None
    smallest_positive = None
    
    # Loop through the list to find the largest negative integer and smallest positive integer
    for num in lst:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    
    # Return the tuple (largest_negative, smallest_positive)
    return (largest_negative, smallest_positive)
