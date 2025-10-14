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
        digits = [int(d) for d in str(num)]
        has_even = False
        for d in digits:
            if d % 2 == 0:
                has_even = True
                break
        if not has_even:
            result.append(num)
    return sorted(result)
