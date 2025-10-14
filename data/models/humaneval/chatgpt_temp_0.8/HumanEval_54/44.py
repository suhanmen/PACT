def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # create a dictionary to keep track of the frequency of each character in s0
    freq = {}
    for c in s0:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    # check if each character in s1 is in the frequency dictionary and has a positive count
    for c in s1:
        if c not in freq or freq[c] == 0:
            return False
        freq[c] -= 1

    # check if all characters in s0 have been accounted for
    for c in freq:
        if freq[c] != 0:
            return False

    return True
