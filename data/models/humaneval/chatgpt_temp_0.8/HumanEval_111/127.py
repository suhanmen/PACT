def histogram(test):
    """Given a string representing space separated lowercase letters, return a dictionary
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
    split_test = test.split()
    counts = {}
    for letter in split_test:
        if letter in counts.keys():
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = max(counts.values())
    max_letters = [key for key, value in counts.items() if value == max_count]
    return {letter: max_count for letter in max_letters}
