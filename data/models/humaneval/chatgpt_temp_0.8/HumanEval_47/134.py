def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    l.sort()
    if n % 2 == 0:
        # If the list has even number of elements, return the average of the middle two
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        # If the list has odd number of elements, return the middle element
        return l[n//2]
