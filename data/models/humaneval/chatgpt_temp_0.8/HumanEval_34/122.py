def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set for unique elements
    unique_set = set(l)
    # Convert the set to a list and sort it
    unique_list = sorted(list(unique_set))
    return unique_list
