# CANNOT PARSE CODE SNIPPET
python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Create a set of unique characters in s0 and s1
    chars0 = set(s0)
    chars1 = set(s1)
    
    # Check if both sets are equal
    return chars0 == chars1
