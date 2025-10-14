# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # sort the characters in each string
    s0_sorted = sorted(s0)
    s1_sorted = sorted(s1)
    
    # compare the sorted strings
    if s0_sorted == s1_sorted:
        return True
    else:
        return False
