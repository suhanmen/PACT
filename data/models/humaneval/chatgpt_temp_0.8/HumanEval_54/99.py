def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    s0_dict = {}
    s1_dict = {}
    for char in s0:
        s0_dict[char] = s0_dict.get(char, 0) + 1
    for char in s1:
        s1_dict[char] = s1_dict.get(char, 0) + 1
    return s0_dict == s1_dict
