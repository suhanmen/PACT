def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Create two dictionaries to store character counts for each string
    chars0 = {}
    chars1 = {}
    
    # Iterate through each string and count the occurrences of each character
    for c in s0:
        if c in chars0:
            chars0[c] += 1
        else:
            chars0[c] = 1
    for c in s1:
        if c in chars1:
            chars1[c] += 1
        else:
            chars1[c] = 1
    
    # Check if the two dictionaries are equal
    return chars0 == chars1
