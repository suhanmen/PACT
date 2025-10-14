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
    # Split the string into a list of letters
    letters = test.split()
    
    # Create a dictionary to hold the letter counts
    letter_counts = {}
    
    # Loop through each letter in the list and count its occurrences
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
            
    # Find the maximum count
    max_count = max(letter_counts.values())
    
    # Create a list to hold the letters with the maximum count
    max_letters = []
    
    # Loop through the letter counts and add any letters with the maximum count to the list
    for letter, count in letter_counts.items():
        if count == max_count:
            max_letters.append(letter)
    
    # Create a dictionary to hold the result
    result = {}
    
    # Loop through the letters with the maximum count and add them to the result dictionary
    for letter in max_letters:
        result[letter] = max_count
