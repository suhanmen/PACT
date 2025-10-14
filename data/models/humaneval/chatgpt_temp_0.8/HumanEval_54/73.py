def same_chars(s0: str, s1: str):
    # Create a dictionary to store the frequency of each character in s0
    freq = {}
    for c in s0:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    # Compare the frequency of each character in s1 to the dictionary
    for c in s1:
        if c not in freq:
            return False
        freq[c] -= 1
        if freq[c] < 0:
            return False
    
    # Check if all the frequencies in the dictionary are zero
    for count in freq.values():
        if count != 0:
            return False
    
    return True
