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
        index1 = length // 2
        index2 = index1 - 1
        return (sorted_l[index1] + sorted_l[index2]) / 2
    else:
        index = length // 2
        return sorted_l[index]
