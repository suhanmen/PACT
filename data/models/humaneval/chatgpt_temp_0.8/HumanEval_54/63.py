# CANNOT PARSE CODE SNIPPET
python
def same_chars(s0: str, s1: str) -> bool:
    # Convert the strings into sets of characters, to discard duplicates
    set0 = set(s0)
    set1 = set(s1)
    
    # Check if the sets are equal (i.e., they have the same characters)
    return set0 == set1
