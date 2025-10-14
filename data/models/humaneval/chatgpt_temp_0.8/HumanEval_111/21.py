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
    # Split the string into a list of individual letters
    letters = test.split()
    
    # Create a dictionary to hold the count of each letter
    letter_counts = {}
    
    # Loop through the letters and count each one
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    # Determine the maximum count
    max_count = max(letter_counts.values())
    
    # Create a dictionary to hold the letters with the maximum count
    result = {}
    
    # Loop through the letter counts and add any with the maximum count to the result dictionary
    for letter, count in letter_counts.items():
        if count == max_count:
            result[letter] = count
    
    # Return the result dictionary
    return result
