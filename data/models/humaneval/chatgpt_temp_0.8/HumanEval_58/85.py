def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    """
    common_elements = sorted(list(set(l1).intersection(set(l2))))
    return common_elements
