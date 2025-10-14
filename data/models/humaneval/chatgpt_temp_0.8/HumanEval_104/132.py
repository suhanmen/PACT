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
    res = []
    for num in x:
        even_flag = False
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_flag = True
                break
        if not even_flag:
            res.append(num)
    return sorted(res)
