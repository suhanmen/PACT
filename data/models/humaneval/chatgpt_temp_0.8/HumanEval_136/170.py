def largest_smallest_integers(lst):
    # Initialize variables to hold largest negative and smallest positive integers
    largest_negative = None
    smallest_positive = None
    
    # Iterate through the list, checking each integer
    for num in lst:
        if num < 0 and (largest_negative is None or num > largest_negative):
            largest_negative = num
        elif num > 0 and (smallest_positive is None or num < smallest_positive):
            smallest_positive = num
    
    # Return a tuple with the largest negative and smallest positive integers
    return (largest_negative, smallest_positive)
