def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Create a set of elements from the first list
    set1 = set(l1)
    
    # Loop through the second list and check if each element is in the first set
    common_elements = []
    for elem in l2:
        if elem in set1:
            common_elements.append(elem)
    
    # Sort the list of common elements and return it
    return sorted(set(common_elements))
