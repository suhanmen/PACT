def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) % 2 == 0:
        # if the length of the list is even, take the average of the two middle elements
        sorted_l = sorted(l)
        middle = len(l) // 2
        return (sorted_l[middle - 1] + sorted_l[middle]) / 2
    else:
        # if the length of the list is odd, return the middle element
        return sorted(l)[len(l) // 2]
