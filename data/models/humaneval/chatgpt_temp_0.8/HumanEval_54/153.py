# CANNOT PARSE CODE SNIPPET
python
def same_chars(s0: str, s1: str) -> bool:
    # If the lengths differ, the strings cannot have the same characters
    if len(s0) != len(s1):
        return False
    
    # Create dictionaries to count the characters in each string
    counts0 = {}
    counts1 = {}
    for char in s0:
        counts0[char] = counts0.get(char, 0) + 1
    for char in s1:
        counts1[char] = counts1.get(char, 0) + 1
    
    # Compare the dictionaries of character counts
    return counts0 == counts1
