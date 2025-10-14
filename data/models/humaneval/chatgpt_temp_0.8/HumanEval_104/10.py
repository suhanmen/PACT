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
    # Create an empty list to store the results
    result = []
    
    # Loop through each integer in the input list
    for i in x:
        # Convert the integer to a string for easier manipulation
        i_str = str(i)
        # Use a flag variable to keep track of whether the integer contains an even digit
        has_even_digit = False
        # Loop through each character in the string representation of the integer
        for digit in i_str:
            # Check if the digit is even
            if int(digit) % 2 == 0:
                # Set the flag to True and break out of the loop
                has_even_digit = True
                break
        # If the integer does not have an even digit, add it to the result list
        if not has_even_digit:
            result.append(i)
    # Sort the result list in increasing order and return it
    result.sort()
    return result
