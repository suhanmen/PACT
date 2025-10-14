def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""

    common_elements = []
    for element in set(l1):
        if element in l2:
            common_elements.append(element)
    
    return sorted(set(common_elements))
