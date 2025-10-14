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
    # Create an empty dictionary to store the letter counts
    counts = {}
    
    # Split the input string by space and iterate over each letter
    for letter in test.split():
        # If the letter is not already in the dictionary, add it with a count of 1
        if letter not in counts:
            counts[letter] = 1
        # If the letter is already in the dictionary, increment its count
        else:
            counts[letter] += 1
    
    # Find the maximum count value
    max_count = max(counts.values())
