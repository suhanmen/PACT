def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_list = list(set(l)) # This line removes duplicates by converting the input list to a set and back to a list.
    unique_list.sort() # This line sorts the resulting list.
    return unique_list # This line returns the sorted unique list.
