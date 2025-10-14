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
        # if n is even, average of middle two elements is the median
        return (l[(n // 2) - 1] + l[n // 2]) / 2
    else:
        # if n is odd, middle element is the median
        return l[n // 2]
