def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Convert both strings to sets to remove duplicates
    set_s0 = set(s0)
    set_s1 = set(s1)
    
    # If the sets are equal, the strings have the same characters
    if set_s0 == set_s1:
        return True
    else:
        return False
