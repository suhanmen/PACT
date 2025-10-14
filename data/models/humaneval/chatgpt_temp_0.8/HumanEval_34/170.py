def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_list = list(set(l)) # Use set to get unique elements, convert it back to list
    unique_list.sort() # Sort the list
    return unique_list # Return the sorted list of unique elements
