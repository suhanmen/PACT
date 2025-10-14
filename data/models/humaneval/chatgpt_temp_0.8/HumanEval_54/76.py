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
    s0_dict = {}
    for char in s0:
        if char in s0_dict:
            s0_dict[char] += 1
        else:
            s0_dict[char] = 1

    s1_dict = {}
    for char in s1:
        if char in s1_dict:
            s1_dict[char] += 1
        else:
            s1_dict[char] = 1

    return s0_dict == s1_dict
