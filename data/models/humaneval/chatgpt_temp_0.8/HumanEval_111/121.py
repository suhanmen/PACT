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
    # Split the string into a list of words
    words = test.split()
    
    # Create an empty dictionary to store letter counts
    counts = {}
    
    # Loop through each word
    for word in words:
        # Loop through each letter in the word
        for letter in word:
            # Increment the count for this letter
            counts[letter] = counts.get(letter, 0) + 1
    
    # Find the highest count
    max_count = max(counts.values())
    
    # Create a new dictionary to store the letters with the highest count
    result = {}
    
    # Loop through each letter and count
    for letter, count in counts.items():
        # If the count is equal to the max count, add it to the result dictionary
        if count == max_count:
            result[letter] = count
    
    # Return the result dictionary
    return result
