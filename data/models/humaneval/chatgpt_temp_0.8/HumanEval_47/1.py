def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()  # sort the list in ascending order
    n = len(l)
    if n % 2 == 0:  # if the list length is even
        return (l[n//2-1] + l[n//2]) / 2
    else:  # if the list length is odd
        return l[n//2]
