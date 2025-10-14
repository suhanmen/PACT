def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    # Create an empty list to hold the unique digits
    unique = []

    # Iterate through the list of integers
    for n in x:
        # Convert the integer to a string for easy digit checking
        s = str(n)
        # Use a flag to keep track of whether the integer has any even digits
        has_even = False
        # Iterate through each digit of the string
        for digit in s:
            # If the digit is even, set the flag to True and exit the loop
            if int(digit) % 2 == 0:
                has_even = True
                break
        # If the integer has no even digits, add it to the unique list
        if not has_even:
            unique.append(n)

    # Sort and return the unique list
    return sorted(unique)
