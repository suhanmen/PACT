def largest_smallest_integers(lst):
    # initialize variables to hold the largest negative integer and smallest positive integer 
    max_negative = None
    min_positive = None
    
    # loop through each integer in the list and update the max_negative and min_positive variables accordingly
    for num in lst:
        if num < 0 and (max_negative is None or num > max_negative):
            max_negative = num
        elif num > 0 and (min_positive is None or num < min_positive):
            min_positive = num
    
    # return a tuple of the max_negative and min_positive values (or None if they don't exist)
    return (max_negative, min_positive)
