def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:  # if the list has 0 or 1 elements, it is trivially monotonic
        return True
    
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    return increasing or decreasing
