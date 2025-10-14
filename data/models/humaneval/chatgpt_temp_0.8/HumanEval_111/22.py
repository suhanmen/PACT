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
    histogram_dict = {}
    test_list = test.split()
    for letter in test_list:
        if letter in histogram_dict:
            histogram_dict[letter] += 1
        else:
            histogram_dict[letter] = 1
    max_occurrence = max(histogram_dict.values())
    result_dict = {}
    for letter, occurrence in histogram_dict.items():
        if occurrence == max_occurrence:
            result_dict[letter] = occurrence
    return result_dict
