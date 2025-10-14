def max_element(l: list):
    """Return maximum element in the list."""
    max_val = l[0]
    for val in l:
        if val > max_val:
            max_val = val
    return max_val
