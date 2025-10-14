def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)
    if n % 2 == 0:
        mid = n // 2
        return (sorted_list[mid-1] + sorted_list[mid]) / 2
    else:
        mid = n // 2
        return sorted_list[mid]
