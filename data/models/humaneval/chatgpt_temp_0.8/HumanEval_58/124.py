# CANNOT PARSE CODE SNIPPET
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    common_elements = list(set(l1) & set(l2))
    return sorted(list(set(common_elements)))
