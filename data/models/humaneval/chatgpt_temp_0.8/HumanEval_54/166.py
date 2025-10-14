# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Count the occurrence of each character in s0
    count_s0 = {}
    for c in s0:
        count_s0[c] = count_s0.get(c, 0) + 1

    # Count the occurrence of each character in s1
    count_s1 = {}
    for c in s1:
        count_s1[c] = count_s1.get(c, 0) + 1

    # Compare the two dictionaries
    return count_s0 == count_s1
