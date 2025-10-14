def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_elem = l[0] # initialize max_elem to the first element of the list
    for elem in l: # loop through each element in the list
        if elem > max_elem: # if the current element is greater than the current max_elem
            max_elem = elem # update max_elem to the current element
    return max_elem
