def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    length = len(sorted_list)
    middle = length // 2
    if length % 2 == 0:
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        return sorted_list[middle]
