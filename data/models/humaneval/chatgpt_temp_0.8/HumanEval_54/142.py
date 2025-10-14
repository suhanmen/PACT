def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Sort the characters in both strings
    sorted_s0 = sorted(s0)
    sorted_s1 = sorted(s1)
    
    # Compare the sorted strings
    return sorted_s0 == sorted_s1
