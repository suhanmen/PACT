def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    for char in set(s0):
        if s0.count(char) != s1.count(char):
            return False
    for char in set(s1):
        if s0.count(char) != s1.count(char):
            return False
    return True
