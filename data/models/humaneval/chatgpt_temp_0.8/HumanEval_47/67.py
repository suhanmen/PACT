def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    l_sorted = sorted(l)
    if n % 2 == 0:
        # even number of elements: average the middle two
        mid = n // 2
        return (l_sorted[mid - 1] + l_sorted[mid]) / 2
    else:
        # odd number of elements: return the middle one
        return l_sorted[n // 2]
