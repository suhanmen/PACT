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
    # Remove all spaces and convert to lowercase
    s0 = s0.replace(' ', '').lower()
    s1 = s1.replace(' ', '').lower()
    
    # Count the frequency of characters in each string
    s0_count = {}
    s1_count = {}
    for c in s0:
        s0_count[c] = s0_count.get(c, 0) + 1
    for c in s1:
        s1_count[c] = s1_count.get(c, 0) + 1
    
    # Check if the two strings have the same characters
    return s0_count == s1_count
