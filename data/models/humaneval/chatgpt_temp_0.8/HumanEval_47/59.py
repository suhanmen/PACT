def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)
    if n % 2 == 0:
        # if the list has an even number of elements, take the average of the middle two
        middle_right = n // 2
        middle_left = middle_right - 1
        return (sorted_list[middle_left] + sorted_list[middle_right]) / 2
    else:
        # if the list has an odd number of elements, take the middle one
        middle = n // 2
        return sorted_list[middle]
