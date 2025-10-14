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
        """Helper function to check if a number contains an even digit."""
        for digit in str(num):
            if int(digit) % 2 == 0:
                return True
        return False
    
    return sorted([num for num in x if not has_even_digit(num)])
