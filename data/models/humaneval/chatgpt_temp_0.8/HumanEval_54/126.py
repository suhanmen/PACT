# CANNOT PARSE CODE SNIPPET
python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Convert the strings into sets of characters
    set0 = set(s0)
    set1 = set(s1)
    
    # Check if the sets are equal
    return set0 == set1
