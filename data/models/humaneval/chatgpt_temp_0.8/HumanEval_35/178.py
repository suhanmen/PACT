def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Initialize the maximum value
    max_val = l[0]
  
    # Iterate through the list
    for val in l:
        # Update the maximum value if a higher value is found
        if val > max_val:
            max_val = val
  
    # Return the maximum value
    return max_val
