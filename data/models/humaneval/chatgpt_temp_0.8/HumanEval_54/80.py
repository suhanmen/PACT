def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    for c in set(s0):
        if s0.count(c) != s1.count(c):
            return False
    return True
