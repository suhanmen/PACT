def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_list = list(set(l)) # convert list to set to remove duplicates and then back to list
    unique_list.sort() # sort the list in ascending order
    return unique_list # return the sorted unique list
