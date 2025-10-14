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
    # First, split the string into individual characters
    characters = test.split()
    
    # Then, create a dictionary to store the counts of each character
    counts = {}
    
    # For each character, update its count in the dictionary
    for character in characters:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    
    # Find the maximum count among all characters
    max_count = max(counts.values())
    
    # Initialize an empty result dictionary
    result = {}
    
    # For each character with a count equal to the maximum count,
    # add it to the result dictionary with its count
    for character, count in counts.items():
        if count == max_count:
            result[character] = count
    
    return result
