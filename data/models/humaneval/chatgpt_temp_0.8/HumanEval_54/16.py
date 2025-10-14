python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Count the frequency of each character in both strings
    count0 = {}
    count1 = {}
    for c in s0:
        count0[c] = count0.get(c, 0) + 1
    for c in s1:
        count1[c] = count1.get(c, 0) + 1
    
    # Compare the two frequency maps
    return count0 == count1
