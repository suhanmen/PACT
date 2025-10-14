# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Count frequencies of characters in both strings
    freq_s0 = {}
    freq_s1 = {}
    for char in s0:
        freq_s0[char] = freq_s0.get(char, 0) + 1
    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1
    
    # Check if the frequencies of characters match
    return freq_s0 == freq_s1
