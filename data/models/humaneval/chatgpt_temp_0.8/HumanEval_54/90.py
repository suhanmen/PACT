def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # convert both strings to sets of characters
    set_s0 = set(s0)
    set_s1 = set(s1)
    
    # check if the sets are equal
    return set_s0 == set_s1
