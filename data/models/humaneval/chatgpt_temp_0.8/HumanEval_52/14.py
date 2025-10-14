def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    """
    for n in l:
        if n >= t:
            return False
    return True
