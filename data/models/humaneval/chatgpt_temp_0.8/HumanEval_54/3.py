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
    # First, we need to remove any spaces or punctuation
    s0 = "".join(c for c in s0 if c.isalnum())
    s1 = "".join(c for c in s1 if c.isalnum())
    
    # Then, we sort the characters in each word
    s0_sorted = sorted(s0)
    s1_sorted = sorted(s1)
    
    # Finally, we compare the sorted strings
    return s0_sorted == s1_sorted
