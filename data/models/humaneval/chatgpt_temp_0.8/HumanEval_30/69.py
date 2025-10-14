def get_positive(l: list):
    """Return only positive numbers in the list."""
    result = []
    for num in l:
        if num > 0:
            result.append(num)
    return result
