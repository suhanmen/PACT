# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    for char in set(s0):
        if char not in s1:
            return False
        if s0.count(char) != s1.count(char):
            return False
    for char in set(s1):
        if char not in s0:
            return False
    return True
