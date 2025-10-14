def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_val = l[0] # initialize max_val to the first element in the list
    for i in range(1, len(l)): # iterate over the remaining elements in the list
        if l[i] > max_val: # if an element is greater than the current max
            max_val = l[i] # update max_val to that element
    return max_val # return the maximum element
