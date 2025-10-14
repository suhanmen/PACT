# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    s0_chars = set(s0)
    s1_chars = set(s1)
    return s0_chars == s1_chars
