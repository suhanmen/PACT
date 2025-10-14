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
    if test == "":
        return {}
    
    words = test.split()
    counts = {}
    max_count = 0
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        
        if counts[word] > max_count:
            max_count = counts[word]
    
    result = {}
    
    for word, count in counts.items():
        if count == max_count:
            result[word] = count
    
    return result
