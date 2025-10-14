def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    length = len(sorted_list)
    if length % 2 == 0:
        median = (sorted_list[length // 2] + sorted_list[length // 2 - 1]) / 2
    else:
        median = sorted_list[length // 2]
    return median
