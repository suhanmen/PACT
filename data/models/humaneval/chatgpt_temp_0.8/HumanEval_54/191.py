def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    for char in s0:
        if char not in s1:
            return False
    for char in s1:
        if char not in s0:
            return False
    return True
