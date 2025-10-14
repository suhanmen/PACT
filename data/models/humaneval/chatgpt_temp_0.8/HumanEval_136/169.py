python
def largest_smallest_integers(lst):
    # Initialize variables a and b with None
    a, b = None, None

    # Loop through each element in the list
    for num in lst:
        # If the number is negative and either a is None or num is greater than a, set a to num
        if num < 0 and (a is None or num > a):
            a = num
        # If the number is positive and either b is None or num is less than b, set b to num
        elif num > 0 and (b is None or num < b):
            b = num
    
    # Return a tuple of (a, b)
    return (a, b)
