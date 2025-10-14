def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    return set(s0) == set(s1) and all(s0.count(char) == s1.count(char) for char in set(s0))
