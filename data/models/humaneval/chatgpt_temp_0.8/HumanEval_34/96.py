def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_list = []
    for element in l:
        if element not in unique_list:
            unique_list.append(element)
    return sorted(unique_list)
