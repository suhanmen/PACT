def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Create dictionaries to hold character counts of each string
    count_s0 = {}
    count_s1 = {}
    
    # Populate the character count dictionaries for each string
    for char in s0:
        count_s0[char] = count_s0.get(char, 0) + 1
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1
        
    # Compare the character count dictionaries to see if they are the same
    return count_s0 == count_s1
