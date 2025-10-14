# CANNOT PARSE CODE SNIPPET
python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Count the occurrences of each character in s0
    counts = {}
    for c in s0:
        counts[c] = counts.get(c, 0) + 1
    # Check if s1 has the same characters and counts
    for c in s1:
        if c not in counts:
            return False
        counts[c] -= 1
        if counts[c] == 0:
            del counts[c]
    return len(counts) == 0
