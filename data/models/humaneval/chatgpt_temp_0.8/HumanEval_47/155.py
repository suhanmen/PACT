def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_sorted = sorted(l)
    n = len(l_sorted)
    if n % 2 == 0:
        return (l_sorted[n//2 - 1] + l_sorted[n//2]) / 2
    else:
        return l_sorted[n//2]
