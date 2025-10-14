def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    result = []
    for i in set(l1):
        if i in l2:
            result.append(i)
    return sorted(set(result))
