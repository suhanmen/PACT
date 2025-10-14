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
        # if the length of the list is even, take the average of the two middle values
        return (sorted_l[length // 2 - 1] + sorted_l[length // 2]) / 2
    else:
        # if the length of the list is odd, take the middle value
        return sorted_l[length // 2]
