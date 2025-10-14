def max_element(l: list):
    """Return maximum element in the list."""
    max_elem = l[0]
    for elem in l:
        if elem > max_elem:
            max_elem = elem
    return max_elem

