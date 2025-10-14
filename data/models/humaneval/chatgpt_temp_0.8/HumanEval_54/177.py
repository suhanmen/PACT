# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Convert the strings to sets of characters
    set_s0 = set(s0)
    set_s1 = set(s1)
    # Check if the sets have the same elements (characters)
    return set_s0 == set_s1
