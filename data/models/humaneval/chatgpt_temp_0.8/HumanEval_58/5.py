def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_elements = []
    for i in l1:
        if i in l2 and i not in common_elements:
            common_elements.append(i)
    return sorted(common_elements)
