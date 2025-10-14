def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        # if the length of the list is even, take the average of the middle two elements
        middle = n // 2
        return (l[middle - 1] + l[middle]) / 2
    else:
        # if the length of the list is odd, take the middle element
        middle = n // 2
        return l[middle]
