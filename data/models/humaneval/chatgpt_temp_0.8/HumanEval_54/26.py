def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # convert strings to sets of characters
    set0 = set(s0)
    set1 = set(s1)
    # check if sets are equal
    return set0 == set1
