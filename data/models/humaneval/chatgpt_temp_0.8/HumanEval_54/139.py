# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    unique_s0 = set(s0)
    unique_s1 = set(s1)
    return unique_s0 == unique_s1
