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
    if not test: # return empty dictionary if the input is empty
        return {}
    letters = test.split() # split the string on space
    letter_counts = {} # initialize an empty dictionary
    max_count = 0 # initialize max_count to 0
    for letter in letters:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
        if letter_counts[letter] > max_count:
            max_count = letter_counts[letter]
    result = {}
    for letter in letter_counts:
        if letter_counts[letter] == max_count:
            result[letter] = max_count
    return result
