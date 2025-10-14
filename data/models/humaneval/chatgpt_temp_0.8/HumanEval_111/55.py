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
    max_occurrence = 0
    max_letters = []
    for letter in set(words):
        count = words.count(letter)
        if count > max_occurrence:
            max_letters = [letter]
            max_occurrence = count
        elif count == max_occurrence:
            max_letters.append(letter)
    return {letter: max_occurrence for letter in max_letters}
