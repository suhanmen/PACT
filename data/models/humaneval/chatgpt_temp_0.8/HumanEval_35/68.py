def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        raise ValueError("List should not be empty")
    max_val = l[0]  # Initialize max_val to the first element of the list
    for val in l:
        if val > max_val:
            max_val = val
    return max_val
