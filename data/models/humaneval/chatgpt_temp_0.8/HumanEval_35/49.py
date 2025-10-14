def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max = l[0] # initialize max to the first element of the list
    for i in range(1, len(l)):
        if l[i] > max:
            max = l[i]
    return max
