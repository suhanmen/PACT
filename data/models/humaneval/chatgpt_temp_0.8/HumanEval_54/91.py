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
    # Remove any spaces or special characters
    s0 = ''.join(filter(str.isalnum, s0))
    s1 = ''.join(filter(str.isalnum, s1))

    # Use set intersection to find the common characters
    common_chars = set(s0) & set(s1)

    # If the common characters set is equal to the set of all characters from both strings,
    # then the strings have the same characters
    return common_chars == set(s0 + s1)
