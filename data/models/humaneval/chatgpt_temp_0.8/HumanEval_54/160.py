def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # First, count the number of occurrences of each character in s0
    count = {}
    for c in s0:
        count[c] = count.get(c, 0) + 1
    # Then, check if s1 has the same characters and counts
    for c in s1:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] == 0:
            del count[c]
    return len(count) == 0
