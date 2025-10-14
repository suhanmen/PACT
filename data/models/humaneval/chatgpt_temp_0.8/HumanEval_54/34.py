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
    else:
        s0_dict = {}
        for char in s0:
            if char in s0_dict:
                s0_dict[char] += 1
            else:
                s0_dict[char] = 1
        
        for char in s1:
            if char in s0_dict:
                s0_dict[char] -= 1
                if s0_dict[char] == 0:
                    del s0_dict[char]
            else:
                return False
        
        if len(s0_dict) == 0:
            return True
        else:
            return False
