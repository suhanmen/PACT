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
    hist = {}
    if len(test) == 0:
        return hist
    test = test.split()
    max_count = 0
    for letter in test:
        if letter in hist:
            hist[letter] += 1
        else:
            hist[letter] = 1
        if hist[letter] > max_count:
            max_count = hist[letter]
    result = {}
    for letter in hist:
        if hist[letter] == max_count:
            result[letter] = max_count
    return result
