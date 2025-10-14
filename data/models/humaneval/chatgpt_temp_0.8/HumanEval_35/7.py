def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_val = l[0]  # set the first element as the initial maximum value
    for num in l:
        if num > max_val:
            max_val = num
    return max_val
