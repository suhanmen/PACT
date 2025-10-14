def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 0:
        # If the list has an even number of elements, return the average of the middle two
        return (sorted_l[n//2 - 1] + sorted_l[n//2]) / 2
    else:
        # If the list has an odd number of elements, return the middle element
        return sorted_l[n//2]
