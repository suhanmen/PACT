# CANNOT PARSE CODE SNIPPET
def same_chars(s0: str, s1: str) -> bool:
    # Count the occurrences of each character in each word
    count0 = {c: s0.count(c) for c in set(s0)}
    count1 = {c: s1.count(c) for c in set(s1)}
    # Check if the two dictionaries are equal
    return count0 == count1
