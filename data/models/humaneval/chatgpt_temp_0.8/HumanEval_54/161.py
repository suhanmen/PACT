def same_chars(s0: str, s1: str):
    # Create dictionaries to count the characters in each string
    count_s0 = {}
    count_s1 = {}
    for c in s0:
        count_s0[c] = count_s0.get(c, 0) + 1
    for c in s1:
        count_s1[c] = count_s1.get(c, 0) + 1

    # Compare the dictionaries
    for c in count_s0:
        if c not in count_s1 or count_s1[c] != count_s0[c]:
            return False
    for c in count_s1:
        if c not in count_s0 or count_s0[c] != count_s1[c]:
            return False
    return True
