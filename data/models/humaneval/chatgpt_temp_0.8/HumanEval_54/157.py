def same_chars(s0: str, s1: str):
    # Convert the strings to sets of characters
    chars0 = set(s0)
    chars1 = set(s1)
    # Check if the sets are equal
    return chars0 == chars1
