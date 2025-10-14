# CANNOT PARSE CODE SNIPPET
python
def same_chars(s0: str, s1: str) -> bool:
    # Remove whitespace and convert to lowercase
    s0 = s0.strip().lower()
    s1 = s1.strip().lower()
    # Count the occurrences of each character in both strings
    count0 = {c: s0.count(c) for c in set(s0)}
    count1 = {c: s1.count(c) for c in set(s1)}
    # Check if the character counts are equal for both strings
    return count0 == count1
