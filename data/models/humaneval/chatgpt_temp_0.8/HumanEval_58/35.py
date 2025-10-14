def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_values = list(set(l1) & set(l2))
    return sorted(common_values)
