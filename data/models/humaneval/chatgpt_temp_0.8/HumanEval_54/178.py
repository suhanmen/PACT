def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    s0_set = set(s0)
    s1_set = set(s1)
    return s0_set == s1_set
