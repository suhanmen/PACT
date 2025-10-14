def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_elems = set(l1) & set(l2)  # find the common elements using set intersection
    return sorted(list(common_elems))  # convert the set back to a list, sort it, and return it
