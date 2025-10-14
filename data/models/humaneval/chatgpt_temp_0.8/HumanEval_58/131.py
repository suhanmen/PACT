# CANNOT PARSE CODE SNIPPET
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    result = []
    for item in set(l1):
        if item in l2:
            result.append(item)
    return sorted(set(result))
