# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    s0_dict = {}
    for char in s0:
        s0_dict[char] = s0_dict.get(char, 0) + 1
    for char in s1:
        if char not in s0_dict:
            return False
        s0_dict[char] -= 1
        if s0_dict[char] == 0:
            del s0_dict[char]
    return len(s0_dict) == 0
