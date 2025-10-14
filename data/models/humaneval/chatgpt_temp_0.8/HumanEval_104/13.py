def has_even_digit(n):
    """Given a positive integer n, returns True if n has any even digit."""
    while n > 0:
        if n % 2 == 0:
            return True
        n //= 10
    return False
    
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
    for n in x:
        if not has_even_digit(n):
            result.append(n)
    return sorted(result)
