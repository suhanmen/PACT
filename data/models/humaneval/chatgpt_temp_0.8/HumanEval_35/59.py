def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_value = l[0] # assume first element is maximum
    for element in l:
        if element > max_value:
            max_value = element
    return max_value
