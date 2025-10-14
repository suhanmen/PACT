def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort the list in ascending order
    sorted_list = sorted(l)
    # get the length of the list
    n = len(sorted_list)
    # if the length of the list is even
    if n % 2 == 0:
        # get the two middle elements
        mid1 = sorted_list[n//2]
        mid2 = sorted_list[n//2 - 1]
        # calculate the average of the two middle elements
        median = (mid1 + mid2) / 2
    # if the length of the list is odd
    else:
        # get the middle element
        median = sorted_list[n//2]
    # return the median
    return median
