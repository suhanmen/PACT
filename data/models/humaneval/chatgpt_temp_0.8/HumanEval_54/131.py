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
    # Count the characters in s0
    s0_counts = {}
    for c in s0:
        s0_counts[c] = s0_counts.get(c, 0) + 1

    # Compare the character counts in s1 with s0
    for c in s1:
        if c not in s0_counts:
            return False
        s0_counts[c] -= 1
        if s0_counts[c] < 0:
            return False

    return True
