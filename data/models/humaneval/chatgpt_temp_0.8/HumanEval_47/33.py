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
        # If the length of the list is even, take the average of the two middle elements
        mid = n // 2
        return (sorted_l[mid-1] + sorted_l[mid]) / 2
    else:
        # If the length of the list is odd, take the middle element
        return sorted_l[n // 2]
