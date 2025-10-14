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
    
    def has_even_digit(num):
        """
        Helper function to check if the number has any even digit.
        """
        while num > 0:
            if num % 2 == 0:
                return True
            num //= 10
        return False
    
    res = []
    for num in x:
        if not has_even_digit(num):
            res.append(num)
    
    return sorted(res)
