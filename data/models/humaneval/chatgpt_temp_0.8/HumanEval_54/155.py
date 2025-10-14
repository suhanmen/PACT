def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Convert strings to sets to remove duplicates
    set_s0 = set(s0)
    set_s1 = set(s1)
    
    # Check if sets are equal
    if set_s0 == set_s1:
        return True
    else:
        return False
