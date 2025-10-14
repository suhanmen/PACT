def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_elements = sorted(set(l1) & set(l2))
    return common_elements

