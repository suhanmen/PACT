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
    # Remove any spaces and make all characters lowercase
    s0 = s0.replace(" ", "").lower()
    s1 = s1.replace(" ", "").lower()

    # Check if the lengths of the strings are equal
    if len(s0) != len(s1):
        return False

    # Convert the strings to sets and check if they are equal
    if set(s0) == set(s1):
        return True
    else:
        return False
