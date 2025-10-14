def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Create sets of unique characters for both strings
    set0 = set(s0)
    set1 = set(s1)
    
    # Check if the sets are equal
    return set0 == set1
