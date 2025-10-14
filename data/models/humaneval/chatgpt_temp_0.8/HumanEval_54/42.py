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
    # Remove any whitespaces from the words
    s0 = s0.replace(" ", "")
    s1 = s1.replace(" ", "")
    
    # Check if the lengths of the words are equal
    if len(s0) != len(s1):
        return False
    
    # Sort the words and compare them
    if sorted(s0) == sorted(s1):
        return True
    else:
        return False
