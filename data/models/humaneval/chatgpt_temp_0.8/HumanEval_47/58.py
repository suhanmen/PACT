def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    list_len = len(sorted_list)
    midpoint = list_len // 2
    if list_len % 2 == 0:
        return (sorted_list[midpoint-1] + sorted_list[midpoint]) / 2
    else:
        return sorted_list[midpoint]
