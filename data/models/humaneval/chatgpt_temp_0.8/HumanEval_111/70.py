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
    words = test.split()
    histogram_dict = {}
    max_count = 0
    
    for word in words:
        if word in histogram_dict:
            histogram_dict[word] += 1
        else:
            histogram_dict[word] = 1
            
        if histogram_dict[word] > max_count:
            max_count = histogram_dict[word]

    result_dict = {}
    for word, count in histogram_dict.items():
        if count == max_count:
            result_dict[word] = count
            
    return result_dict
