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
    is_increasing = None
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            if is_increasing == False:
                return False
            is_increasing = True
        elif l[i] < l[i-1]:
            if is_increasing == True:
                return False
            is_increasing = False
    return True
