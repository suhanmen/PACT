def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    for char in s0:
        if char not in s1:
            return False
        elif s0.count(char) != s1.count(char):
            return False
    return True
