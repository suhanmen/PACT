def histogram(test):
    """Given a string representing space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    if not test:  # empty string
        return {}
    
    letters = test.split()  # split string into list of letters
    letter_count = {}  # dictionary to store count of each letter
    
    # loop through letters and count occurrences
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    # find the maximum count
    max_count = max(letter_count.values())
    
    # create a dictionary with all letters that hav
