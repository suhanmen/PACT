def histogram(test):
    """
    Given a string representing space separated lowercase letters, return a dictionary
    of the letter(s) with the most repetition and the corresponding count.
    If several letters have the same occurrence, return all of them.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    counts = {}
    for letter in test.split():
        counts[letter] = counts.get(letter, 0) + 1

    max_count = max(counts.values())
    result = {letter: count for letter, count in counts.items() if count == max_count}

    return result
