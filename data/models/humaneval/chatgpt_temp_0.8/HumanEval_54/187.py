def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # create a dictionary to store the characters and their counts for s0
    chars_s0 = {}
    for char in s0:
        chars_s0[char] = chars_s0.get(char, 0) + 1
    
    # create a dictionary to store the characters and their counts for s1
    chars_s1 = {}
    for char in s1:
        chars_s1[char] = chars_s1.get(char, 0) + 1
    
    # compare the two dictionaries and return True if they are the same
    return chars_s0 == chars_s1
