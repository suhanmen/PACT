def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    if len(l) % 2 == 0:
        # if the list has an even number of elements, return the average of the middle two
        middle = len(l) // 2
        return (l[middle - 1] + l[middle]) / 2
    else:
        # if the list has an odd number of elements, return the middle element
        return l[len(l) // 2]
