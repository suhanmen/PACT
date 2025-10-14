# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # create a dictionary to count the characters in s0
    char_count = {}
    for char in s0:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # iterate over the characters in s1
    for char in s1:
        # if a character occurs in s1 but not s0, return False
        if char not in char_count:
            return False
        # if the character count in s1 is greater than in s0, return False
        if s1.count(char) > char_count[char]:
            return False

    # if we made it this far, the strings must have the same characters
    return True
