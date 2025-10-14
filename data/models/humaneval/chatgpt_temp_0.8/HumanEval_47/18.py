def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    s = sorted(l)
    if n % 2 == 0:
        return (s[n//2-1] + s[n//2])/2
    else:
        return s[n//2]
