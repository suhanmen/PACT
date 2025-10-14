# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Convert the strings to sets of characters
    set0 = set(s0)
    set1 = set(s1)
    
    # Check if the sets are equal
    if set0 == set1:
        return True
    else:
        return False
