def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    length = len(l)
    if length % 2 == 0:
        median = (l[length//2 - 1] + l[length//2]) / 2
    else:
        median = l[length//2]
    return median
