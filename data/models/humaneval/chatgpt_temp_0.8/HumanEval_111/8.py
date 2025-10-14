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
    test = test.split()
    dict_test = {}
    for letter in test:
        if letter not in dict_test:
            dict_test[letter] = 1
        else:
            dict_test[letter] += 1
    max_count = max(dict_test.values())
    max_letters = [letter for letter, count in dict_test.items() if count == max_count]
    return {letter: max_count for letter in max_letters}
