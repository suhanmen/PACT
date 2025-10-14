def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_elems = list(set(l1) & set(l2))
    return sorted(set(common_elems))
