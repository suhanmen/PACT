# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Create a dictionary to count the characters in s0
    char_count = {}
    for char in s0:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Loop through the characters in s1 and decrement their count in char_count
    for char in s1:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    
    # Check if all the counts in char_count are zero
    for count in char_count.values():
        if count != 0:
            return False
    
    return True
