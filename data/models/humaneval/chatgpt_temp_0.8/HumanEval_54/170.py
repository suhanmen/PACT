def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    s0_dict = {}
    s1_dict = {}

    for char in s0:
        if char in s0_dict:
            s0_dict[char] += 1
        else:
            s0_dict[char] = 1

    for char in s1:
        if char in s1_dict:
            s1_dict[char] += 1
        else:
            s1_dict[char] = 1

    return s0_dict == s1_dict
