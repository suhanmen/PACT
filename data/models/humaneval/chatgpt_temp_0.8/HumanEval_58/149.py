def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_elements = []
    for elem in l1:
        if elem in l2 and elem not in common_elements:
            common_elements.append(elem)
    return sorted(common_elements)
