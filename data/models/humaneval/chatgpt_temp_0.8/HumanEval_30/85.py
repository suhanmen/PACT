def get_positive(l: list):
    """Return only positive numbers in the list."""
    result = []
    for number in l:
        if number > 0:
            result.append(number)
    return result
