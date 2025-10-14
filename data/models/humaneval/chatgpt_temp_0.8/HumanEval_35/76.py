def max_element(l: list):
    """Return maximum element in the list."""
    if len(l) == 0:
        return None
    max_element = l[0]
    for element in l:
        if element > max_element:
            max_element = element
    return max_element
