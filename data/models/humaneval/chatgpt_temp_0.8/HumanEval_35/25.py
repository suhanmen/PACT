def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_element = l[0] # initialize max_element to first element of list
    for element in l[1:]: # iterate through all elements in the list
        if element > max_element:
            max_element = element # update max_element if element is larger
    return max_element
