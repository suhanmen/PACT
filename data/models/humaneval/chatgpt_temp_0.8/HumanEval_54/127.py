def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Create dictionaries to count the occurrence of each character in each string
    s0_dict = {}
    s1_dict = {}
    for char in s0:
        s0_dict[char] = s0_dict.get(char, 0) + 1
    for char in s1:
        s1_dict[char] = s1_dict.get(char, 0) + 1
    
    # Check if the dictionaries are the same
    return s0_dict == s1_dict
