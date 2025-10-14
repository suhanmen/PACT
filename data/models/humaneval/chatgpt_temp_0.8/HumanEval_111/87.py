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
  
    letters = test.split()
    count = {}
    max_count = 0
    
    for letter in letters:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
        if count[letter] > max_count:
            max_count = count[letter]
    
    result = {}
    for letter, count in count.items():
        if count == max_count:
            result[letter] = count
    
    return result
