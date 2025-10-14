def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t."""
    for number in l:
        if number >= t:
            return False
    return True
