def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    s0_dict = {}
    for c in s0:
        if c in s0_dict:
            s0_dict[c] += 1
        else:
            s0_dict[c] = 1
    
    s1_dict = {}
    for c in s1:
        if c in s1_dict:
            s1_dict[c] += 1
        else:
            s1_dict[c] = 1
    
    return s0_dict == s1_dict

