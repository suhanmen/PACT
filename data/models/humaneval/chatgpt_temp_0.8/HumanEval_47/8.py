def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    list_len = len(sorted_list)
    mid = list_len // 2

    if list_len % 2 == 0:
        # If the length of the list is even
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        # If the length of the list is odd
        return sorted_list[mid]
