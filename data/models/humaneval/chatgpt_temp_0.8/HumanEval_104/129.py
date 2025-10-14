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
    for i in x:
        even_digit_found = False
        for j in str(i):
            if int(j) % 2 == 0:
                even_digit_found = True
                break
        if not even_digit_found:
            result.append(i)
    return sorted(result)
