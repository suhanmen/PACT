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
    # Create a dictionary to store the letter counts
    letter_counts = {}
    
    # Split the input string into individual letters
    letters = test.split()
    
    # Loop through each letter and increment its count in the dictionary
    for letter in letters:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    # Find the maximum count among all letters
    max_count = max(letter_counts.values())
    
    # Create a list of letters with the maximum count
    max_letters = [key for key, value
