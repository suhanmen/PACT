def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    length = len(sorted_l)
    if length % 2 == 0:
        median_upper = sorted_l[length // 2]
        median_lower = sorted_l[length // 2 - 1]
        return (median_upper + median_lower) / 2
    else:
        return sorted_l[length // 2]
