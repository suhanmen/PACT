python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Convert strings to sets of characters
    set0, set1 = set(s0), set(s1)
    
    # Check if the two sets are equal
    return set0 == set1
