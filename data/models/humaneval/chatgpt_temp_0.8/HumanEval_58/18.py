def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_elements = []
    for element in l1:
        if element in l2 and element not in common_elements:
            common_elements.append(element)
    return sorted(common_elements)
