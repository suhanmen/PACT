def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Create an empty set and a result list
    unique_set = set()
    result = []
    
    # Iterate through the input list and add unique elements to the set
    for elem in l:
        if elem not in unique_set:
            unique_set.add(elem)
    
    # Convert the set back to a list and sort it
    result = list(unique_set)
    result.sort()
    
    return result
