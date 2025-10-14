# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    if len(s0) != len(s1):
        return False
    
    for char in s0:
        if s0.count(char) != s1.count(char):
            return False
    
    return True
