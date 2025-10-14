def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    length = len(sorted_list)
    if length % 2 == 0:
        # if the length of the list is even, return the average of the middle two elements
        return (sorted_list[length//2-1] + sorted_list[length//2])/2
    else:
        # if the length of the list is odd, return the middle element
        return sorted_list[length//2]
