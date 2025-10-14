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
    freq_dict = {}
    for letter in test.split():
        freq_dict[letter] = freq_dict.get(letter, 0) + 1
    max_freq = max(freq_dict.values())
    return {key: val for key, val in freq_dict.items() if val == max_freq}
