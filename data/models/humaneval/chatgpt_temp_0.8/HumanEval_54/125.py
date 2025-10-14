# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # First, we create a set of the unique characters in each word
    # by casting them to set objects.
    chars0 = set(s0)
    chars1 = set(s1)
    
    # We then check if the set intersection of the two sets has
    # the same length as either set. If it does, that means all
    # the characters in one set are also in the other set, so the
    # words have the same characters.
    return len(chars0 & chars1) == len(chars0) == len(chars1)
