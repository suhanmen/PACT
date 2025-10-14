# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    if len(s0) != len(s1):
        return False
    for char in s0:
        if char not in s1:
            return False
        s1 = s1.replace(char, '', 1)
    return True
