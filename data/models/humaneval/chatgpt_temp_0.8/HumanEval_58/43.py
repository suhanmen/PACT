def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_list = []
    for element in l1:
        if element in l2 and element not in common_list:
            common_list.append(element)
    return sorted(common_list)
