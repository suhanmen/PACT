def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Initialize the maximum element as the first element in the list
    max_element = l[0]
    # Loop through the list starting from the second element
    for i in range(1, len(l)):
        # If the current element is greater than the current maximum element, update the maximum element
        if l[i] > max_element:
            max_element = l[i]
    # Return the maximum element
    return max_element
