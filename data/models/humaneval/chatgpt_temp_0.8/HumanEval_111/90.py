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
    result = {}
    if test:
        letters = test.split()
        max_count = 0
        for letter in letters:
            count = letters.count(letter)
            if count >= max_count:
                max_count = count
                result[letter] = count
        # remove items with count less than the max count
        for key in list(result.keys()):
            if result[key] < max_count:
                del result[key]
    return result
