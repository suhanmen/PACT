def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Convert strings to sets of characters and compare
    return set(s0) == set(s1)
