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
    
    # Create a dictionary to hold the counts for each letter
    letter_counts = {}
    
    # Split the string into individual letters
    letters = test.split()
    
    # Count the occurrences of each letter
    for letter in letters:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    
    # Find the maximum count
    max_count = max(letter_counts.values())
    
    # Create a dictionary to hold the letters with the maximum count
    max_letters = {}
    
    # Add any letters with the maximum count to the dictionary
    for letter, count in letter_counts.items():
        if count == max_count:
            max_letters[letter] = count
    
    return max_letters
