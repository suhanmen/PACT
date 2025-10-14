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
    if len(s0) != len(s1):
        return False
    s0_counts = {}
    for char in s0:
        if char in s0_counts:
            s0_counts[char] += 1
        else:
            s0_counts[char] = 1
    for char in s1:
        if char not in s0_counts or s0_counts[char] == 0:
            return False
        s0_counts[char] -= 1
    return True
