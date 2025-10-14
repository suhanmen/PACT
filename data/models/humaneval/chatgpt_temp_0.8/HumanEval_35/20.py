def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Initialize max_element to first element of list
    max_element = l[0]
    
    # Loop through the list and update max_element if a larger value is found
    for element in l:
        if element > max_element:
            max_element = element
    
    return max_element
