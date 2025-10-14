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

    # Initialize an empty list to store the unique digits
    unique_digits_list = []

    # Loop through each integer in the input list
    for integer in x:
        # Convert the integer to a string so we can check its digits
        integer_string = str(integer)
        # Assume the integer has no even digits until proven otherwise
        has_even_digits = False
        # Loop through each digit in the integer
        for digit in integer_string:
            # Check if the digit is even
            if int(digit) % 2 == 0:
                has_even_digits = True
        # If the integer has no even digits, add it to the list of unique digits
        if not has_even_digits:
            unique_digits_list.append(integer)

    # Sort and return the list of unique digits
    return sorted(unique_digits_list)
