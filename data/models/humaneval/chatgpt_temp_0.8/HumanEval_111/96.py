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
    if not test:
        return result
    
    letters = test.split()
    max_count = 0
    for letter in letters:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
        if result[letter] > max_count:
            max_count = result[letter]
    
    max_letters = [k for k, v in result.items() if v == max_count]
    return {k: v for k, v in result.items() if k in max_letters}
