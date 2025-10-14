def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    inc = True
    dec = True

    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            inc = False
        if l[i] > l[i-1]:
            dec = False
        if not inc and not dec:
            return False

    return True
