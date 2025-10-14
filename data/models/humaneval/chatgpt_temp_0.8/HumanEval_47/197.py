def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    sorted_l = sorted(l)
    if n % 2 == 0:
        # even number of elements: median is the average of the middle two
        mid = n // 2
        return (sorted_l[mid-1] + sorted_l[mid]) / 2
    else:
        # odd number of elements: median is the middle one
        return sorted_l[n // 2]
