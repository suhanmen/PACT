def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    
    inc = dec = True
    
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            inc = False
        if l[i] > l[i-1]:
            dec = False
            
    return inc or dec
