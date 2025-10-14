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
    # Split the input string into a list of individual lowercase letters
    letters = test.lower().split()
    
    # Create an empty dictionary to store letter counts
    counts = {}
    
    # Iterate through the letters and update the counts dictionary
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    # Find the maximum count in the dictionary
    max_count = max(counts.values())
    
    # Create a sub-dictionary with all letters that have the maximum count
    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count
    
    return result
