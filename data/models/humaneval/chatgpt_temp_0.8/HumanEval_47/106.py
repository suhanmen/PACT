def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    n = len(l)
    if n % 2 == 0:
        median1 = l[n//2]
        median2 = l[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = l[n//2]
    return median
