def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    if set(s0) == set(s1):
        return True
    else:
        return False
