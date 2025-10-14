python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Use sets to compare the unique characters in each string
    return set(s0) == set(s1)
