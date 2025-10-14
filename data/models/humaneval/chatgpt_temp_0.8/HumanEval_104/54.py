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
    
    # create an empty list to store the unique digits
    unique_list = []
    
    # loop through each number in the input list
    for num in x:
        # convert the number to a string to check each digit
        num_str = str(num)
        # use a flag to track whether the number has any even digits
        has_even_digit = False
        # loop through each digit in the number
        for digit in num_str:
            # check if the digit is even
            if int(digit) % 2 == 0:
                has_even_digit = True
                break
        # if the number doesn't have any even digits, add it to the list
        if not has_even_digit:
            unique_list.append(num)
    
    # sort the list and return it
    return sorted(unique_list)
