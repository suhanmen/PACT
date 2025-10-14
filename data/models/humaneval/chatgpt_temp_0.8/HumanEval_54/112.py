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
    # First, count the number of occurrences of each character in each string
    count0 = {}
    count1 = {}
    for c in s0:
        if c in count0:
            count0[c] += 1
        else:
            count0[c] = 1
    for c in s1:
        if c in count1:
            count1[c] += 1
        else:
            count1[c] = 1
    # Then, check if the two dictionaries are equal
    return count0 == count1
