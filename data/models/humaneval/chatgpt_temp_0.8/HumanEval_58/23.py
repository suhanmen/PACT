def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    unique_l1 = set(l1)
    unique_l2 = set(l2)
    common_elements = sorted(list(unique_l1.intersection(unique_l2)))
    return common_elements
