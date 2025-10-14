def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True
    n = len(l)
    for i in range(1, n):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
    return increasing or decreasing
