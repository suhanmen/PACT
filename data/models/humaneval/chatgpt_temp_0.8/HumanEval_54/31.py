# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    s0_set = set(s0)
    s1_set = set(s1)
    
    if s0_set == s1_set:
        return True
    else:
        return False
