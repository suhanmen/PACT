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
    for number in x:
        has_even_digit = False
        for digit in str(number):
            if int(digit) % 2 == 0:
                has_even_digit = True
                break
        if not has_even_digit:
            result.append(number)
    return sorted(result)
