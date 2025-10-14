def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:  # empty list case
        return None
    max_elem = l[0]  # assume first element is the maximum
    for elem in l:
        if elem > max_elem:
            max_elem = elem
    return max_elem
