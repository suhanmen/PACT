def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    return set(s0) == set(s1) and all(s0.count(c) == s1.count(c) for c in set(s0))
