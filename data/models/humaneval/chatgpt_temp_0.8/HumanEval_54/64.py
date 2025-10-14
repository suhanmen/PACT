def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Create dictionaries to count characters in each string
    s0_count = {}
    s1_count = {}
    
    # Count characters in s0
    for char in s0:
        if char in s0_count:
            s0_count[char] += 1
        else:
            s0_count[char] = 1
    
    # Count characters in s1
    for char in s1:
        if char in s1_count:
            s1_count[char] += 1
        else:
            s1_count[char] = 1
    
    # Check if the two dictionaries are the same
    return s0_count == s1_count
