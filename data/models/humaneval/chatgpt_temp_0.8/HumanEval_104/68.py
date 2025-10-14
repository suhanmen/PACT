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
    def has_even_digit(n):
        """Returns True if n has even digit, otherwise False."""
        for digit in str(n):
            if int(digit) % 2 == 0:
                return True
        return False

    result = []
    for num in sorted(x):
        if not has_even_digit(num):
            result.append(num)
    return result
