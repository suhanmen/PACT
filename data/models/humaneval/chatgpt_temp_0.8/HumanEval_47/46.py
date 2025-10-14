def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    list_length = len(sorted_list)
    
    if list_length % 2 == 0:
        # If the list has an even number of elements, take the average of the middle two
        middle_index = list_length // 2
        return (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        # If the list has an odd number of elements, return the middle element
        middle_index = list_length // 2
        return sorted_list[middle_index]
