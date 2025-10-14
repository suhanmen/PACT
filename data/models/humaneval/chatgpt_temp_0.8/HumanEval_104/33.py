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
    # Initialize an empty list to store the final result
    result = []
    # Iterate through each element of the input list x
    for num in x:
        # Convert the number to a string in order to check each digit
        str_num = str(num)
        # Check if any digit is even, if not, append to the result list
        if all(int(digit) % 2 != 0 for digit in str_num):
            result.append(num)
    # Sort the result list in increasing order and return it
    return sorted(result)
