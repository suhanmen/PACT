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
    
    # split the string into a list of letters
    letters = test.split()
    
    # create a dictionary to store the letter counts
    counts = {}
    
    # loop through the letters and count their occurrences
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    # find the maximum count of any letter
    max_count = max(counts.values())
    
    # create a dictionary to store the letters with the maximum count
    max_letters = {}
    
    # loop through the letters and add any with the maximum count to the dictionary
    for letter, count in counts.items():
        if count == max_count:
            max_letters[letter] = count
    
    return max_letters
