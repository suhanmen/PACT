# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Remove spaces and convert to lowercase
    s0 = s0.lower().replace(' ', '')
    s1 = s1.lower().replace(' ', '')
    
    # Sort the characters of both strings
    s0_sorted = ''.join(sorted(s0))
    s1_sorted = ''.join(sorted(s1))
    
    # Check if the sorted strings are equal
    return s0_sorted == s1_sorted
