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
    count_s0 = {}
    count_s1 = {}

    for char in s0:
        count_s0[char] = count_s0.get(char, 0) + 1

    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1

    return count_s0 == count_s1
