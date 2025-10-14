def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Step 1: Convert the strings to sets of characters
    set0 = set(s0)
    set1 = set(s1)
    
    # Step 2: Check if the sets are equal
    return set0 == set1
