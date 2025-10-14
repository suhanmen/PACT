def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    for char in s0:
        if char not in s1:
            return False
        s1 = s1.replace(char, '', 1)
    return True
