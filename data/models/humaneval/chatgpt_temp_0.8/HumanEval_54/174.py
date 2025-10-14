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
    # Check if the length of both strings is equal
    if len(s0) != len(s1):
        return False

    # Count the number of occurrences of each character in both strings
    count_s0 = {}
    count_s1 = {}
    for c in s0:
        count_s0[c] = count_s0.get(c, 0) + 1
    for c in s1:
        count_s1[c] = count_s1.get(c, 0) + 1

    # Check if the counts of each character are the same in both strings
    for c in count_s0:
        if c not in count_s1 or count_s0[c] != count_s1[c]:
            return False

    return True
