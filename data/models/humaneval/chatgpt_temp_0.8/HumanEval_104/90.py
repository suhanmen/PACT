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
    result = []
    for num in x:
        digits = [int(d) for d in str(num)] # convert num to list of digits
        if all(digit % 2 != 0 for digit in digits): # check if all digits are odd
            result.append(num)
    return sorted(result)
