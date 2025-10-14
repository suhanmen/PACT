def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    s0_count = {}
    for c in s0:
        s0_count[c] = s0_count.get(c, 0) + 1
    s1_count = {}
    for c in s1:
        s1_count[c] = s1_count.get(c, 0) + 1
    return s0_count == s1_count
