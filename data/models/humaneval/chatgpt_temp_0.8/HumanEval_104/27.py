def unique_digits(x):
    """
    Given a list of positive integers x, returns a sorted list of all 
    elements that have no even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []
    for num in x:
        even = False
        for digit in str(num):
            if int(digit) % 2 == 0:
                even = True
                break
        if not even:
            result.append(num)
    return sorted(result)
