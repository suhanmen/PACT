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
    test_list = test.split()
    freq_dict = {}
    max_freq = 0
    for letter in test_list:
        if letter not in freq_dict:
            freq_dict[letter] = 1
        else:
            freq_dict[letter] += 1
        if freq_dict[letter] > max_freq:
            max_freq = freq_dict[letter]
    return {k: v for k, v in freq_dict.items() if v == max_freq}
