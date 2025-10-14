def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    s1 = set(l1)
    s2 = set(l2)
    common_elements = list(s1 & s2)
    return sorted(list(set(common_elements)))
