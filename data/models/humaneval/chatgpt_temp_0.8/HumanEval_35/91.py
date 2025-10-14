def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_val = l[0] # initialize the maximum value to the first element in the list
    for i in l: # loop through the list
        if i > max_val: # if the current element is greater than the maximum value
            max_val = i # set the maximum value to the current element
    return max_val # return the maximum value
