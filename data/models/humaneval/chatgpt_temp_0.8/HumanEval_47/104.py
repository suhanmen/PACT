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
        # if there are an even number of elements, average the middle two
        return (l[n//2-1] + l[n//2]) / 2
    else:
        # if there are an odd number of elements, return the middle one
        return l[n//2]
