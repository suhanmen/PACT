def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_elements = set(l1) & set(l2)  # Find the intersection of the two lists
    return sorted(list(common_elements))  # Convert the set to a list and sort it
