def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    if not test:
        return {}
    
    # Split the string into words and count the occurrence of each letter
    counts = {}
    for char in test.split():
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    
    # Find the maximum count
    max_count = max(counts.values())
    
    # Create a dictionary with the letters that have the maximum count
    result = {}
    for char, count in counts.items():
        if count == max_count:
            result[char] = count
    
    return result
