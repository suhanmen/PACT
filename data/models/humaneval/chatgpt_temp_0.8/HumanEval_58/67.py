def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Find the common elements between the two lists
    common_elements = list(set(l1).intersection(set(l2)))
    # Sort the common elements
    common_elements.sort()
    # Return the sorted unique common elements
    return list(set(common_elements))
