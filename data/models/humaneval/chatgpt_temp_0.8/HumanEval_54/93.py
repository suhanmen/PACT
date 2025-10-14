# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # First, convert each string to a set of characters
    chars0 = set(s0)
    chars1 = set(s1)
    
    # Then, check if the sets are equal
    return chars0 == chars1
