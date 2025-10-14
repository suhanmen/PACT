def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Convert strings to sets for efficient character comparison
    set_s0 = set(s0)
    set_s1 = set(s1)
    
    # Check if the sets are equal
    return set_s0 == set_s1
