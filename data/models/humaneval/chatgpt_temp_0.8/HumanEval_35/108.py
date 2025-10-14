# CANNOT PARSE CODE SNIPPET
def max_element(l: list) -> int:
    """Return maximum element in the list."""
    if not l:
        return None
    max_num = l[0]  # start with the first element
    for i in range(1, len(l)):
        if l[i] > max_num:
            max_num = l[i]
    return max_num
