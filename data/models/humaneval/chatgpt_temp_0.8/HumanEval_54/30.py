def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # convert the strings to sets of characters
    set0 = set(s0)
    set1 = set(s1)
    # check if the sets have the same elements
    return set0 == set1
