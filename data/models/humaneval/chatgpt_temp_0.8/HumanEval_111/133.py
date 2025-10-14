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
    letters = test.split()
    histogram_dict = {}
    max_count = 0
    for letter in letters:
        if letter in histogram_dict:
            histogram_dict[letter] += 1
        else:
            histogram_dict[letter] = 1
        if histogram_dict[letter] > max_count:
            max_count = histogram_dict[letter]

    result_dict = {}
    for letter in histogram_dict:
        if histogram_dict[letter] == max_count:
            result_dict[letter] = max_count
    return result_dict
