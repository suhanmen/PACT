# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Count the number of occurrences of each character in s0 and s1
    count0 = {}
    count1 = {}
    for c in s0:
        count0[c] = count0.get(c, 0) + 1
    for c in s1:
        count1[c] = count1.get(c, 0) + 1
    
    # Check if the counts are the same for all characters
    for c in set(s0 + s1):
        if count0.get(c, 0) != count1.get(c, 0):
            return False
    return True
